#!/usr/bin/env python3
"""Outliers de una cuenta: mediana de vistas y cuántas veces la supera cada reel.

Uso:
  python3 scripts/outliers.py .tmp/cuenta.csv --cuenta @cuenta

El CSV tiene columnas url,vistas,fecha (fecha AAAA-MM-DD, opcional). Las vistas pueden venir
como 12.345, 12,3 mil, 1,5 M, 12.3K o 1.5M. Una fila sin vistas legibles se cuenta como "sin dato".
Los umbrales salen de config.json -> outliers.
"""
import argparse, csv, datetime as dt, json, os, re, statistics, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CFG = json.load(open(os.path.join(RAIZ, "config.json")))["outliers"]


def vistas(txt):
    t = (txt or "").strip().lower().replace(" ", "")
    if not t:
        return None
    m = re.match(r"^([\d.,]+)(m|mill|millones|k|mil)?$", t)
    if not m:
        return None
    num, suf = m.group(1), m.group(2)
    if suf:
        num = num.replace(",", ".")
        if num.count(".") > 1:
            return None
        n = float(num)
        return int(round(n * (1_000_000 if suf.startswith("m") and suf != "mil" else 1_000)))
    return int(num.replace(".", "").replace(",", ""))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--cuenta", default="")
    ap.add_argument("--hoy", default=dt.date.today().isoformat())
    a = ap.parse_args()
    hoy = dt.date.fromisoformat(a.hoy)
    filas, sin_dato, nuevos = [], [], []
    with open(a.csv, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            v = vistas(r.get("vistas"))
            fecha = (r.get("fecha") or "").strip()
            if v is None:
                sin_dato.append(r.get("url", ""))
                continue
            if fecha:
                try:
                    if (hoy - dt.date.fromisoformat(fecha)).days < CFG["dias_minimos_publicado"]:
                        nuevos.append(r.get("url", ""))
                        continue
                except ValueError:
                    pass
            filas.append({"url": r.get("url", ""), "vistas": v, "fecha": fecha})
    filas = filas[: CFG["reels_a_mirar_por_cuenta"]]
    if len(filas) < 5:
        sys.exit(f"Muy pocos reels con vistas ({len(filas)}). Hacen falta al menos 5 para una mediana que sirva.")
    med = statistics.median(f["vistas"] for f in filas)
    for f in filas:
        f["veces"] = f["vistas"] / med if med else 0
    filas.sort(key=lambda f: -f["veces"])
    mi, pr = CFG["minimo_veces_mediana"], CFG["prioridad_veces_mediana"]
    print(f"# {a.cuenta or a.csv} · {len(filas)} reels · mediana {med:,.0f} vistas".replace(",", "."))
    print(f"Outlier = {mi}× la mediana o más ({mi*med:,.0f}+). Prioridad = {pr}× o más.\n".replace(",", "."))
    print("| | Veces | Vistas | Fecha | Link |\n|---|---|---|---|---|")
    hay = False
    for f in filas:
        if f["veces"] < mi:
            continue
        hay = True
        marca = "PRIORIDAD" if f["veces"] >= pr else "outlier"
        print(f"| {marca} | {f['veces']:.1f}× | {f['vistas']:,} | {f['fecha'] or 'sin dato'} | {f['url']} |".replace(",", "."))
    if not hay:
        print("| — | — | — | — | Ningún reel llega a la regla. Probá con otra cuenta. |")
    if nuevos:
        print(f"\nNo cuentan todavía (menos de {CFG['dias_minimos_publicado']} días): {len(nuevos)}")
    if sin_dato:
        print(f"Sin dato de vistas: {len(sin_dato)}")


if __name__ == "__main__":
    main()
