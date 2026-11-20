#!/usr/bin/env python3
"""Arma TABLERO.html: todo tu contenido en un solo lugar (se abre con doble clic o `open TABLERO.html`).

Lee las carpetas y arma 6 columnas: ideas elegidas · guiones para grabar · crudos por editar ·
editados para revisar · listo para publicar · publicado. Arriba, la semana de calendario.md.
El agente lo vuelve a correr cada vez que cambia algo:  python3 scripts/tablero.py
"""
import datetime as dt, html, os, re

R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
J = lambda *p: os.path.join(R, *p)
VID = (".mp4", ".mov", ".m4v")


def lista(carpeta, ext=None, dirs=False):
    p = J(carpeta)
    if not os.path.isdir(p):
        return []
    out = []
    for n in sorted(os.listdir(p), reverse=True):
        if n.startswith("."):
            continue
        full = os.path.join(p, n)
        if dirs and os.path.isdir(full):
            out.append(n)
        elif not dirs and os.path.isfile(full) and (ext is None or n.lower().endswith(ext)):
            out.append(n)
    return out


def ideas_marcadas():
    p = J("3-ideas", "ideas.md")
    if not os.path.exists(p):
        return []
    out = []
    for l in open(p, encoding="utf-8"):
        if re.match(r"^\|\s*\[x\]", l, re.I):
            celdas = [c.strip() for c in l.strip().strip("|").split("|")]
            if len(celdas) > 1:
                out.append(" · ".join(c for c in celdas[1:3] if c))
    return out


def semana():
    p = J("8-publicar", "calendario.md")
    if not os.path.exists(p):
        return "Todavía no hay calendario. Pedile al agente: «Armame la semana»."
    txt = open(p, encoding="utf-8").read()
    partes = re.split(r"(?m)^## ", txt)
    return ("## " + partes[1]).strip() if len(partes) > 1 else txt.strip()


def publicado():
    p = J("8-publicar", "publicado.md")
    if not os.path.exists(p):
        return []
    filas = [l for l in open(p, encoding="utf-8") if l.startswith("|") and not re.match(r"^\|\s*(Fecha|---)", l)]
    return [" · ".join(c.strip() for c in f.strip().strip("|").split("|")[:4]) for f in filas][-10:][::-1]


def md_tabla(md):
    """Pasa las tablas y títulos de calendario.md a HTML simple."""
    out, filas = [], []
    def cerrar():
        if filas:
            out.append("<table>" + "".join(filas) + "</table>")
            filas.clear()
    for l in md.splitlines():
        if l.startswith("|"):
            if re.match(r"^\|\s*-", l):
                continue
            celdas = [html.escape(c.strip()) for c in l.strip().strip("|").split("|")]
            tag = "th" if not filas else "td"
            filas.append("<tr>" + "".join(f"<{tag}>{c}</{tag}>" for c in celdas) + "</tr>")
        else:
            cerrar()
            if l.startswith("### "):
                out.append(f"<h3>{html.escape(l[4:])}</h3>")
            elif l.startswith("## "):
                out.append(f"<h2>{html.escape(l[3:])}</h2>")
            elif l.strip():
                out.append(f"<p>{html.escape(l)}</p>")
    cerrar()
    return "\n".join(out)


cols = [
    ("Ideas elegidas", ideas_marcadas(), "Marcá con [x] en 3-ideas/ideas.md"),
    ("Guiones para grabar", lista("3-ideas/guiones", ".md"), "Pedí: «Pasá a guion las marcadas»"),
    ("Crudos por editar", lista("1-entrada"), "Tirá acá lo que grabaste"),
    ("Editados para revisar", lista("4-videos/editados", VID), "Miralos y pedí cambios"),
    ("Listo para publicar", lista("8-publicar/cola", dirs=True), "Decí «publicalo» o «programá la semana»"),
    ("Publicado", publicado(), "Se anota solo al publicar"),
]
tarjetas = "".join(
    f'<section><h3>{t} <span>{len(xs)}</span></h3>'
    + ("".join(f"<div class=c>{html.escape(x)}</div>" for x in xs) or f"<p class=v>{v}</p>")
    + "</section>"
    for t, xs, v in cols
)
hoy = dt.datetime.now().strftime("%d/%m/%Y %H:%M")
pagina = f"""<!doctype html><html lang=es><meta charset=utf-8><title>Tablero de contenido</title>
<style>
body{{font-family:-apple-system,Arial,sans-serif;margin:24px;background:#f6f6f4;color:#111}}
h1{{margin:0 0 4px}} .s{{color:#666;margin:0 0 20px}}
.k{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px}}
section{{background:#fff;border:1px solid #ddd;border-radius:10px;padding:12px}}
section h3{{margin:0 0 8px;font-size:14px;display:flex;justify-content:space-between}}
section h3 span{{background:#F1C232;border-radius:20px;padding:0 8px}}
.c{{border:1px solid #e5e5e5;border-radius:6px;padding:6px 8px;margin:6px 0;font-size:13px;word-break:break-word}}
.v{{color:#999;font-size:12px}} .sem{{background:#fff;border:1px solid #ddd;border-radius:10px;padding:12px 16px;margin-bottom:16px;overflow-x:auto}}
table{{border-collapse:collapse;font-size:13px;margin:6px 0}} td,th{{border-bottom:1px solid #eee;padding:4px 10px;text-align:left}}
</style>
<h1>Tablero de contenido</h1><p class=s>Actualizado {hoy} · se rehace con <code>python3 scripts/tablero.py</code></p>
<div class=sem>{md_tabla(semana())}</div>
<div class=k>{tarjetas}</div></html>"""
open(J("TABLERO.html"), "w", encoding="utf-8").write(pagina)
print("Listo: TABLERO.html")
