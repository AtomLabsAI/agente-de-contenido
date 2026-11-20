#!/usr/bin/env python3
"""Etapa de la cuenta según seguidores y vistas (reglas en config.json -> etapas).

Uso:
  python3 scripts/etapa.py --seguidores 1240 --seguidores-hace-14 1010 --reels datos.json [--hoy AAAA-MM-DD]

datos.json = [{"fecha": "AAAA-MM-DD", "vistas": 1234}, ...] con los reels del feed (sin trials)
de las últimas semanas.
"""
import argparse, datetime as dt, json, os, statistics

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E = json.load(open(os.path.join(RAIZ, "config.json")))["etapas"]


def semanas(reels, hoy, n):
    """Mediana de vistas de cada una de las últimas n semanas (la más vieja primero)."""
    out = []
    for i in range(n, 0, -1):
        fin = hoy - dt.timedelta(days=7 * (i - 1))
        ini = fin - dt.timedelta(days=7)
        vs = [r["vistas"] for r in reels if ini < dt.date.fromisoformat(r["fecha"]) <= fin]
        out.append((ini + dt.timedelta(days=1), fin, statistics.median(vs) if vs else None, len(vs)))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seguidores", type=int, required=True)
    ap.add_argument("--seguidores-hace-14", type=int)
    ap.add_argument("--reels")
    ap.add_argument("--hoy", default=dt.date.today().isoformat())
    a = ap.parse_args()
    hoy = dt.date.fromisoformat(a.hoy)
    reels = json.load(open(a.reels)) if a.reels else []
    vc = E["vistas_constantes"]
    sem = semanas(reels, hoy, vc["semanas"]) if reels else []
    todas = [r["vistas"] for r in reels
             if (hoy - dt.date.fromisoformat(r["fecha"])).days <= 7 * vc["semanas"]]
    med_mes = statistics.median(todas) if todas else None
    constantes = bool(sem) and med_mes is not None and all(
        m is not None and m >= vc["piso_vs_mediana_del_mes"] * med_mes for _, _, m, _ in sem)

    print(f"Seguidores: {a.seguidores}" + (f" (hace 14 días: {a.seguidores_hace_14})" if a.seguidores_hace_14 is not None else ""))
    if sem:
        print(f"Mediana de vistas por reel, últimas {vc['semanas']} semanas: {med_mes:.0f}")
        for ini, fin, m, n in sem:
            print(f"  {ini} a {fin}: {'sin reels' if m is None else f'{m:.0f} ({n} reels)'}")
        print(f"Vistas constantes: {'sí' if constantes else 'no'} (ninguna semana por debajo del {vc['piso_vs_mediana_del_mes']:.0%} de la mediana del período, y sin semanas vacías)")
    else:
        print("Sin datos de reels: no se puede saber si las vistas son constantes.")

    h, c = E["historias_desde_seguidores"], E["calendario_desde_seguidores"]
    sostenido = a.seguidores_hace_14 is None or a.seguidores_hace_14 >= h
    if a.seguidores >= c and constantes:
        etapa = "3 · Sistema"
    elif a.seguidores >= h and sostenido:
        etapa = "2 · Conexión"
    else:
        etapa = "1 · Ojos"
    print(f"\nETAPA: {etapa}")
    if etapa.startswith("1"):
        falta = "seguidores" if a.seguidores < h else f"sostener {h}+ durante {E['historias_semanas_sostenido']} semanas"
        print(f"Próximo salto (2 · Conexión): {h} seguidores sostenidos. Falta: {falta}.")
    elif etapa.startswith("2"):
        faltan = []
        if a.seguidores < c:
            faltan.append(f"{c - a.seguidores} seguidores")
        if not constantes:
            faltan.append("vistas constantes")
        print(f"Próximo salto (3 · Sistema): {c} seguidores con vistas constantes. Falta: {', '.join(faltan)}.")
    if a.seguidores_hace_14 is None and a.seguidores >= h:
        print("Ojo: sin el dato de hace 14 días no se puede confirmar que los seguidores estén sostenidos.")


if __name__ == "__main__":
    main()
