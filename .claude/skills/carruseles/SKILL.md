---
name: carruseles
description: Crea carruseles para Instagram (1080×1350) a partir de un tema, un reel que funcionó o una idea, con gancho fuerte en la portada, pocas palabras por slide, el sistema visual de la marca y CTA de "Comentá PALABRA". Renderiza cada slide de HTML a PNG y revisa cada imagen antes de entregar. Usar cuando pidan "armame un carrusel", "pasá este reel a carrusel", "hacé 4 carruseles de estos temas" o "carrusel viral para Instagram".
---

# Crear carruseles

Convertís un tema en un carrusel de 5 a 10 slides que se lee rápido, se guarda y termina en
un comentario. Formato post **1080×1350** (4:5).

**En esta carpeta:** cada carrusel va a `5-carruseles/<slug>/` (HTML + PNG). La identidad
(colores, tipografías, fotos en `perfil/fotos/`) sale de `perfil/perfil.md`.

**La primera vez** que la persona pide un carrusel, antes de diseñar:
1. Pedile 3 a 5 carruseles de referencia que le gusten (links o capturas) y guardalos en
   `perfil/referencias/carruseles/`. Si no tiene, mostrale los 3 estilos de la sección 3.
2. Confirmá su identidad (colores, tipografías, si quiere su cara en la portada).
3. Armá **una sola slide de prueba** con ese estilo y que la apruebe. Recién ahí el carrusel entero.
4. Anotá el estilo elegido en `perfil/perfil.md` («Estilo de carruseles: ___») para no volver a
   preguntar.

Antes de cada carrusel preguntá lo que falte: **tema o reel de base, la promesa del gancho, la
palabra del CTA y qué se regala por DM**. Respetá la etapa del diagnóstico (en la etapa 1, solo
carruseles TOFU). Si hay carruseles que ya funcionaron en la cuenta, mirá 4 o 5 antes de diseñar:
copiá la estructura y el tono, no el texto.

---

## 1. De dónde salen los temas

- **De los reels que ya rindieron.** Un reel con muchas vistas es un tema validado: el
  carrusel es otra forma de contar lo mismo.
- Listas «top 5 / 10 / 20», «X cosas que…», «Creés que X. Es Y.» (cambio de modelo mental).
- Un tema por carrusel. Si da para dos, son dos carruseles.

## 2. Estructura

| Slide | Qué va |
|---|---|
| 1 · Portada | Gancho = promesa + número, en 2 o 3 líneas. Una imagen fuerte. Nada más |
| 2 · Contexto | Por qué importa, en una frase. O el «antes» del problema |
| 3 a N-1 · Contenido | **Un punto por slide**: título corto + 1 o 2 líneas + algo visual (captura, ícono, ejemplo) |
| N · CTA | «Comentá PALABRA y te mando…» con la palabra en el color de acento |

- **Poco texto.** Si una slide tiene más de 25 palabras, partila o recortala.
- Números grandes y numeración visible (1/7, 2/7…) cuando es lista: dan ganas de seguir pasando.
- Ejemplos concretos marcados «ej.» en vez de frases genéricas.

## 3. Estilo visual

Elegí uno y sostenelo en todo el carrusel.

**A · Estilo historia (portadas y storytelling):**
- Foto **real** del creador de fondo (de un banco de fotos propias, nunca una cara generada).
- Texto en **burbuja negra redondeada**, letra blanca gruesa.
- Palabra clave del tema en el acento 1 (celeste / azul), palabra del CTA en el acento 2
  (naranja / coral).

**B · Sistema de marca (slides informativas):** la paleta de `perfil/perfil.md` como variables.
Ejemplo (la de Atom):
```
--fondo:#2b2a2a   --fondo-2:#211f1f   --panel:#343232
--texto:#fce9e4   --texto-2:#c9b8b4   --acento:#87abdb   --acento-2:#db6f54
```
- Títulos en una sans gruesa (Montserrat 800 / Inter 800-900), texto Inter 600, código en
  JetBrains Mono.
- Tarjetas con radio 24–32, borde fino y sombra suave. Un solo color de acento por slide.

**C · Estilo personaje (el que más rinde en cuentas de IA):**
- Fondo de color sólido de la marca (por ejemplo azul oscuro) igual en todas las slides.
- Un **muñequito pixel** como protagonista que hace la acción de cada slide.
- Muy poco texto: título + 1 línea. Fondos de foto solo de paisajes o texturas, nunca oficinas genéricas.

Reglas para los tres:
- Márgenes de 80 px a los costados; nada importante en los 120 px de abajo.
- Logos de terceros: el logo real, nunca uno aproximado.
- Mismo tamaño de título en todas las slides internas.

## 4. Pipeline técnico

1. Una carpeta por carrusel: `5-carruseles/<slug>/`.
2. Un HTML por slide, o un `gen.py` que arma todas desde una plantilla y una lista de datos
   (lo más rápido para listas).
3. Render a PNG con Chrome headless o Playwright:
   ```bash
   "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
     --screenshot="slide-01.png" --window-size=1080,1350 \
     --hide-scrollbars "file:///ruta/slide-01.html"
   ```
   Para gráficos que van sobre una foto o un video, fondo transparente
   (`--default-background-color=00000000`) y confirmá que el PNG tenga alpha real.
4. **Mirá cada PNG** antes de darlo por bueno. Lo que más se rompe: texto cortado, tarjetas
   fuera del lienzo, una fuente que no cargó (cae a Times), emojis que salen como cuadrados.
5. Si hace falta editarlo a mano después, armalo en una herramienta de diseño editable
   (Canva, Figma, Claude Design) en vez de PNG fijos.

## 5. Caption y CTA

- Caption corto: una línea que repite el gancho + «Comentá "PALABRA" y te mando…».
- Sin hashtags.
- La palabra del CTA dispara una automatización de comentario → DM que manda el recurso
  (guía, prompt, plantilla) o un botón a la comunidad.
- Una palabra distinta por recurso para poder medir qué se pide.

## 6. Revisar antes de entregar

- Leer las slides en orden como si fueras el que scrollea: ¿la portada sola da ganas de pasar?
- Ortografía, tildes, voseo parejo.
- Ningún dato inventado: cifras, precios y nombres de herramientas verificados contra la fuente.
- La palabra del CTA es la misma en la última slide, en el caption y en la automatización.

## Reglas de contenido

- Nada con derechos: fotos ajenas, personajes de terceros, capturas de películas.
- Caras reales solo del creador y de sus fotos propias.
- Nada se publica sin el ok explícito de quien lo pidió.
