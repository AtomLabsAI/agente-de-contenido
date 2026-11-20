#!/usr/bin/env python3
"""Plantilla base de carruseles (1080×1350). Copiá esta carpeta a 5-carruseles/<slug>/, editá
slides.json (colores y tipografías de perfil/perfil.md) y corré:
    python3 gen.py            # arma slide-01.html, slide-02.html…
    ./render.sh               # pasa cada HTML a PNG con Chrome
Tipos de slide: portada (con foto opcional de perfil/fotos/), contexto, punto, cta.
En los títulos, [palabra] va en el color de acento.
"""
import html, json, os, re

D = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(os.path.join(D, "slides.json"), encoding="utf-8"))
C, T = S["colores"], S["tipografias"]
N = len(S["slides"])


def acento(t, color):
    return re.sub(r"\[(.+?)\]", lambda m: f'<span style="color:{color}">{m.group(1)}</span>', html.escape(t))


CSS = f"""
@import url('https://fonts.googleapis.com/css2?family={T['titulo'].replace(' ', '+')}:wght@800&family={T['texto'].replace(' ', '+')}:wght@500;700&display=swap');
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{C['fondo']};color:{C['texto']};font-family:'{T['texto']}',Arial,sans-serif;position:relative;overflow:hidden}}
.pad{{position:absolute;inset:0;padding:110px 80px 160px;display:flex;flex-direction:column;justify-content:center;gap:36px}}
h1{{font-family:'{T['titulo']}',Arial,sans-serif;font-weight:800;font-size:92px;line-height:1.05}}
h2{{font-family:'{T['titulo']}',Arial,sans-serif;font-weight:800;font-size:72px;line-height:1.1}}
p{{font-size:44px;line-height:1.35;color:{C['texto2']};font-weight:500}}
.num{{font-family:'{T['titulo']}',Arial,sans-serif;font-weight:800;font-size:150px;color:{C['acento']};line-height:1}}
.pie{{position:absolute;left:80px;right:80px;bottom:60px;display:flex;justify-content:space-between;font-size:28px;color:{C['texto2']}}}
.foto{{position:absolute;inset:0;background-size:cover;background-position:center}}
.velo{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 30%,rgba(0,0,0,.85) 100%)}}
.palabra{{display:inline-block;background:{C['acento2']};color:#fff;font-family:'{T['titulo']}',Arial,sans-serif;font-weight:800;font-size:96px;padding:10px 36px;border-radius:24px}}
"""

for i, s in enumerate(S["slides"], 1):
    tipo = s["tipo"]
    if tipo == "portada":
        foto = s.get("foto")
        fondo = f'<div class=foto style="background-image:url(\'{foto}\')"></div><div class=velo></div>' if foto else ""
        cuerpo = f'{fondo}<div class=pad style="justify-content:flex-end"><h1>{acento(s["titulo"], C["acento"])}</h1></div>'
    elif tipo == "contexto":
        cuerpo = f'<div class=pad><h2>{acento(s["titulo"], C["acento"])}</h2><p>{html.escape(s["texto"])}</p></div>'
    elif tipo == "punto":
        cuerpo = f'<div class=pad><div class=num>{html.escape(s["numero"])}</div><h2>{acento(s["titulo"], C["acento"])}</h2><p>{html.escape(s["texto"])}</p></div>'
    elif tipo == "cta":
        cuerpo = f'<div class=pad style="align-items:flex-start"><h2>{acento(s["titulo"], C["acento"])}</h2><div class=palabra>{html.escape(s["palabra"])}</div><p>{html.escape(s["texto"])}</p></div>'
    else:
        raise SystemExit(f"Tipo de slide desconocido: {tipo}")
    pie = f'<div class=pie><span>{html.escape(S.get("cuenta", ""))}</span><span>{i}/{N}</span></div>'
    open(os.path.join(D, f"slide-{i:02d}.html"), "w", encoding="utf-8").write(
        f"<!doctype html><html><meta charset=utf-8><style>{CSS}</style><body>{cuerpo}{pie}</body></html>")
print(f"{N} slides armadas. Ahora: ./render.sh")
