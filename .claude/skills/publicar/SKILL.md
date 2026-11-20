---
name: publicar
description: Publica o programa en Instagram una pieza aprobada (reel, carrusel, trial reel, historia) con su automatización comentario → DM — por Zernio de fábrica, o preparando todo para ManyChat, para subir a mano o para otro inbox (WhatsApp, mail, chat). Usar cuando digan "publicalo", "programalo para el …", "programá la semana", "armá la automatización" o "subilo".
---

# Publicar

**Regla de oro:** nada se publica ni se programa sin que la persona diga «publicalo» o
«programalo» **para esa pieza** (o para esa lista, después de verla). Si pide «programá la
semana», primero mostrale la lista con fecha, hora, caption, palabra y DM, y esperá su ok.

Cada pieza lista vive en `8-publicar/cola/AAAA-MM-DD-tema/` con:
- el archivo final (mp4 o PNG en orden);
- `pieza.md`: tipo (reel, carrusel, trial, historia), etapa, caption, PALABRA (con y sin tilde),
  texto del DM, link del recurso y cuándo sale.

Mirá `config.json` → `conectores.publicar` y `conectores.dm_automatico`.

## A · Zernio (de fábrica)

Las herramientas de Zernio que no estén en la lista se buscan con `search_tools` y se llaman con
`call_tool`. Usá siempre el `account_id` de `config.json`.

1. **Cuenta sana:** `accounts_get_account_health` (o `accounts_list`). Si está desconectada,
   avisale: se reconecta en el panel de Zernio. No sigas.
2. **Subir los archivos originales:** `media_get_media_presigned_url` con `filename`,
   `content_type` (`video/mp4`, `image/png`, `image/jpeg`) y `size` →
   `curl -sS -X PUT -H "Content-Type: <tipo>" --data-binary @<archivo> "<uploadUrl>"` → usá el
   `publicUrl`. La media vence a los 7 días si ningún post la usa: subila recién al publicar.
3. **Crear el post:** `posts_create_post` con:
   - `content`: el caption;
   - `media_items`: `[{type, url}]` en orden (un carrusel son varias imágenes en el mismo post);
   - `platforms`: `[{platform: "instagram", accountId, platformSpecificData}]`;
   - ahora → `publish_now: true`; con fecha → `scheduled_for` + `timezone` de `config.json`;
   - trial reel → `platformSpecificData.trialParams.graduationStrategy: "MANUAL"`;
   - historia → buscá el campo con `docs_search` («instagram story») antes de la primera.
4. **Automatización comentario → DM** (si la pieza trae PALABRA):
   `comment_automations_create_comment_automation` con `account_id`, `name`, `post_id` (queda
   pendiente y se arma sola cuando sale el post), `keywords` (la palabra con y sin tilde; vacío =
   cualquier comentario), `match_mode: "word"`, `typo_tolerance: true`, `dm_message` (texto
   plano, con el link), `comment_reply: "Te lo mandé por privado"`.
5. **Registrar:** fila en `8-publicar/publicado.md` (fecha · tipo · etapa · tema · link · palabra)
   y mové la carpeta de `cola/` a `8-publicar/publicado/`. Corré `python3 scripts/tablero.py`.

## Trial reels

Un trial reel es un reel que Instagram le muestra primero a gente que **no** te sigue. Sirve para
probar un gancho sin quemar a tus seguidores, o para volver a sacar un reel que ya rindió.
- Variante del video: skill `editar-videos`, sección «Variantes para trial reels» (velocidad,
  filtro, zoom, recorte y otro encode; nunca se tocan los textos).
- Al publicar por Zernio: `platformSpecificData.trialParams.graduationStrategy: "MANUAL"` (lo pasás
  vos al feed si rinde) o `"SS_PERFORMANCE"` (lo pasa Instagram).
- A los 2 o 3 días, compará vistas y skip contra el original y anotalo en `8-publicar/publicado.md`.

## B · ManyChat (u otra herramienta de DM)

Zernio (o la persona a mano) publica; la automatización la arma la persona en su herramienta.
Vos le dejás en `pieza.md`, listo para copiar:
- la PALABRA y sus variantes (con y sin tilde, mayúscula y minúscula);
- el texto del DM;
- la respuesta pública al comentario.
Y le recordás el paso a paso de `docs/CONECTORES.md`.

Ojo: si tiene ManyChat y Zernio conectados a la misma cuenta, las respuestas a historias las
toma ManyChat. Que elija uno para cada cosa.

## C · Manual

Dejás la carpeta en `cola/` con el archivo, el caption listo para pegar y la hora sugerida. Cuando
la persona avise que la subió, pedile el link y registrala.

## D · Otro inbox (WhatsApp, mail, chat de la web)

Si los mensajes le llegan por otro lado, el CTA cambia: «Escribime "PALABRA" por WhatsApp y te
mando ___» o «Dejá tu mail en el link de la bio». Preparale el mensaje de respuesta para que lo
pegue (o lo cargue en su herramienta) y anotá en `config.json` qué usa.

## Lo que se rompe seguido

| Síntoma | Causa | Qué hacer |
|---|---|---|
| Error de cuenta desconectada | Meta cortó el acceso | Reconectar en el panel de Zernio |
| El DM no le llega a quien no te sigue | El DM llevaba botones | Texto plano |
| Error de cuenta ambigua | Hay más de una cuenta de Instagram | Pasar siempre `accountId` |
| El link de la media no anda | Venció (7 días sin usarse) | Volver a subirla al publicar |

## Reglas

- Instagram manda **un solo DM automático por comentario**: que ese DM sea el recurso.
- Una palabra distinta por recurso, así sabés qué se pide más.
- Sin hashtags. DM sin emojis raros ni signos de apertura que algunos teléfonos rompen.
