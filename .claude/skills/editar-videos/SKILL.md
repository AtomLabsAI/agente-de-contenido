---
name: editar-videos
description: Edita reels verticales (1080×1920) a partir de un crudo hablado o de un b-roll — elige las tomas limpias, corta, pone títulos y tarjetas por paso, subtítulos de 2-3 palabras pegados a la voz, sonido y revisión cuadro por cuadro antes de entregar. También arma videos animados (motion graphics) con HyperFrames o Remotion. Usar cuando pidan "editame este video", "armame el reel", "ponele subtítulos", "hacé un b-roll con tarjetas", "animá este guion" o "hacé variantes para trial reels".
---

# Editar videos (reels, b-roll y animados)

**En esta carpeta:** el crudo está en `1-entrada/` y su guion (si hay) en `3-ideas/guiones/`. El
reel final va a `4-videos/editados/<tema>.mp4` y el crudo, ya usado, a
`4-videos/crudos/AAAA-MM-DD-tema/`. Lo intermedio, a `.tmp/` (se borra al terminar). Colores,
tipografías y tono salen de `perfil/perfil.md`; el estilo de edición, de los videos de
`perfil/referencias/`. Cuando el reel está aprobado, armá su carpeta en `8-publicar/cola/`.

Herramientas: ffmpeg y whisper-cli (`brew install ffmpeg whisper-cpp`) con un modelo de whisper
(`scripts/analizar.sh` lo baja la primera vez). Si falta algo, avisá antes de arrancar.

Convertís un crudo (con tomas repetidas, pausas y errores) o una idea en un reel vertical
listo para Instagram/TikTok/Shorts. Hay tres tipos de video y cada uno tiene su camino:

| Tipo | Qué es | Herramienta |
|---|---|---|
| **Talking head** | La persona habla a cámara, con títulos, tarjetas y subtítulos | ffmpeg + capas PNG (HTML → PNG) |
| **B-roll con tarjetas** | La persona trabajando (tecleando, caminando), sin voz, con un gancho y tarjetas que van pasando | ffmpeg + capas PNG, música la pone el creador en la app |
| **Animado / motion graphics** | Todo generado: personajes, listas, pantallas, la voz real por arriba | **HyperFrames** (HTML → video) o **Remotion** (React → video) |

Antes de arrancar preguntá lo que falte: **gancho (título), los pasos o bloques, qué se
muestra en cada uno, la palabra del CTA y la marca (colores, tipografía, logo)**. Si ya hay
un video parecido que funcionó, pedilo y mirá 20 cuadros para copiar la estructura, no el
contenido.

---

## 1. El formato que rinde

- **Gancho = promesa + número** («7 agentes que podés crear en 10 minutos», «Tu Jarvis en 7
  pasos»). Visible desde el **primer cuadro**, nada de intros. La pregunta como gancho rinde peor.
- **Voz desde el segundo 0** y el paso 1 en el segundo 2.
- **Un paso por bloque**: título numerado + la imagen que prueba lo que dice (captura, logo,
  terminal, prompt escrito).
- **Listas que se desbloquean**: cada punto arranca bloqueado y aparece cuando se dice. Si el
  título promete más puntos de los que se dicen, el último queda bloqueado hasta el CTA.
- **Contenido concreto en pantalla**: si dice un prompt, el prompt escrito; si habla de datos,
  datos de ejemplo marcados «ej.». Nada genérico.
- **CTA al final**: «Comentá PALABRA y te mando…», con la palabra en el color de acento.
- Duración: b-roll 10–15 s, tutorial 30–60 s.

## 2. Zonas del cuadro (1080×1920, 30 fps)

| Zona | Y | Qué va |
|---|---|---|
| Fuera de margen arriba | 0–230 | Nada importante (la tapa la UI) |
| Título / gancho | 230–330 | Blanco o con placa, 60–80 px, centrado |
| Imagen / tarjeta | 290–690 | Captura, logo, tarjeta, terminal |
| Cara | ~690–1200 | **Libre** (medila en cada toma, no la supongas) |
| Subtítulos | ~1260 | 2-3 palabras, 50 px, blanco con sombra |
| Fuera de margen abajo | 1650+ | Nada (caption y botones) |

- Márgenes laterales: todo lo importante entre **x 60 y 960**; de y 1000 para abajo, nada a la
  derecha de x 940 (ahí van los botones de like y comentar).
- Si el pedido dice que la tarjeta puede tapar la cara (b-roll), se puede usar y 440–1000.

## 3. Colores y tipografía

Definí la paleta como variables y no te salgas de ella. Una por marca:

```
--fondo:#2b2a2a   --fondo-2:#211f1f   --panel:#343232
--texto:#fce9e4   --acento:#87abdb   --acento-2:#db6f54
```
- Títulos: una sans gruesa (Montserrat 800 / Inter 800-900). Texto: Inter 600-700.
  Código y terminal: JetBrains Mono.
- **Un color de acento para la palabra clave** y otro para la palabra del CTA. El resto en
  blanco o crema.
- Tarjetas: placa oscura semitransparente (rgba(35,33,33,.94)), radio 26–40, sombra suave.
  Sobre paredes claras, la placa oscura se lee sola; sobre fondo oscuro, sumá un degradé.
- Logos de terceros: el logo real, nunca uno aproximado.

## 4. Talking head: cortes paso a paso

1. **Transcribir** el crudo con timestamps por palabra (whisper).
2. **Elegir tomas**: de cada frase repetida quedate con la **última toma limpia**. Verificá
   cada borde transcribiendo el tramo exacto: whisper inventa frases en las pausas largas.
3. **Cortar en una sola pasada** (un `filter_complex` con trim + concat de imagen y audio
   juntos). Encodear clips por separado y pegarlos desincroniza la boca.
4. **Buscar repeticiones** después de armar: las pegadas («que revise, que revise») y la misma
   frase en dos bloques. Confirmá escuchando antes de recortar.
5. **Zoom alternado** (1.0 / 1.07) entre cortes para que el salto no se note.
6. **HDR del iPhone**: pasalo a SDR antes de cortar (en Mac, `avconvert`), si no queda lavado.

## 5. Capas (títulos y tarjetas)

- Cada capa es un HTML de 1080×1920 con fondo transparente, renderizado a PNG con Chrome
  headless o Playwright. Confirmá que el PNG tenga alpha real.
- **Corte seco entre capas**, nunca un fundido: dos tarjetas en la misma posición cruzándose
  quedan ilegibles.
- Tiempos de capa **en la grilla de 30 fps** (redondeados a cuadros exactos), si no, aparece un
  cuadro sin título en cada corte.
- Una línea de tiempo `[["clave", inicio, fin], …]` y un solo `overlay` por capa con
  `enable='between(t,a,b)'`.

## 6. Subtítulos

- Grupos de 2-3 palabras, pegados al **ataque de voz** (no a los tiempos crudos de whisper,
  que se corren en los empalmes).
- Se corrige ortografía y tildes; **nunca se reescribe** lo que dice. Sin punto final.
- Números con su unidad juntos («20 dólares», «24 horas»).
- Si hay una tarjeta fija a un costado, el renglón se corre al hueco libre en vez de achicarse.

## 7. Sonido

- Voz nivelada a **-15 LUFS**. Música 15 LU por debajo, con ducking (baja sola cuando hablan).
- Efectos cortos: golpe al gancho, pop o whoosh al entrar una tarjeta, golpe al CTA. Se generan
  con ffmpeg (`aevalsrc`, `anoisesrc`), sin bancos con derechos.
- **B-roll para subir con música**: efectos solo al principio y al final, y la música la elige
  el creador en la app.
- Nada de música conocida dentro del archivo.

## 8. Animados: HyperFrames o Remotion

Para videos 100 % generados (personajes pixel, listas que se desbloquean, chats, terminales).

**HyperFrames** (HTML + CSS + GSAP → MP4):
- Cada escena es HTML con una sola línea de tiempo pausada (seek-safe). Se renderiza con su CLI
  (`hyperframes render`).
- Ideal si ya tenés todo en HTML/CSS (las mismas plantillas de carruseles sirven).
- En Mac con poca RAM: **un render a la vez**, `-w 1`, con `nice`.

**Remotion** (React → MP4):
- Componentes React con `useCurrentFrame()` e `interpolate()`. Render con `npx remotion render`.
- Ideal si el equipo ya trabaja en React o el video se genera desde datos (plantillas por cliente).

En los dos:
- La **voz real** va por arriba y las animaciones se sincronizan con las palabras
  (`palabras.json` de whisper): la boca del personaje se mueve con el volumen, cada punto
  aparece cuando se dice.
- **Animaciones solo para explicar** (un cable de la app al WhatsApp), nada decorativo.
- Escenario del tema (oficina si habla de trabajo, playa si habla del finde), nada genérico.
- Velocidad final ×1,1–1,2 para que no se haga largo.
- Imágenes generadas con IA solo para fondos y sin caras reales ni personajes con derechos.
  Si el moderador bloquea algo, no se esquiva: se hace a mano en HTML.

## 9. Variantes para trial reels

Para probar el mismo reel varias veces sin que la plataforma lo tome como duplicado:
- velocidad ×0,98–1,10 (`setpts` + `atempo`), filtro de color leve, zoom 1,00–1,08;
- recortar 0,2–0,6 s al principio y al final;
- otro encode (crf, preset, `-g`, bitrate de audio) y metadata nueva
  (`-map_metadata -1` + `title`, `creation_time`, `handler_name` propios);
- si hay tiempo, otro estilo de título o de subtítulo.
Nunca se tocan los textos ni el orden del video.

## 10. Revisar antes de entregar (no saltear)

- **Mosaico** de 10-20 cuadros repartidos, sobre todo en los cambios de capa.
- **Primeros 3 segundos cuadro por cuadro**: gancho visible en el cuadro 0, voz desde el 0.
- Nada fuera de márgenes, nada tapando la cara (salvo pedido), textos completos y legibles.
- Escuchar los empalmes: palabras dobladas o cortadas.
- Duración, loudness y que el CTA se vea entero en el último cuadro.

## Lo que se rompe seguido

| Síntoma | Causa | Arreglo |
|---|---|---|
| La boca no coincide con la voz | clips encodeados por separado | cortar en una sola pasada |
| Video lavado, blanquecino | HDR del iPhone sin tone mapping | pasar a SDR antes de cortar |
| Un cuadro sin título en cada corte | tiempos fuera de la grilla de 30 fps | redondear a cuadros |
| Dos textos encimados | fundido entre tarjetas | corte seco |
| Subtítulo adelantado | tiempos de whisper en empalmes | pegarlo al ataque de voz |
| Frase repetida | el corte entró antes de la toma buena | revisar repeticiones y escuchar |
| Tarjeta tapa la cara | se supuso dónde estaba la cabeza | medirla en un cuadro de esa toma |

## Reglas de contenido

- Nada con derechos: música conocida, fotogramas de películas, personajes ajenos.
- Capturas reales. Si se recrea una pantalla, avisarlo y usar datos de ejemplo marcados «ej.».
- Cifras, precios y nombres de modelos: verificados contra la fuente o afuera.
- Nada se publica sin el ok explícito de quien pidió el video.
