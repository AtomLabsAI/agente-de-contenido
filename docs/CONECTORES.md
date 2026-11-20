# Conectores

El agente viene con **Zernio** de fábrica, conectado por el **conector oficial de Claude**
(claude.ai → Configuración → Conectores → Zernio: un clic, sin API ni claves). Pero se adapta a lo que uses. Se configura en
`config.json` → `conectores` (o decile al agente «uso ManyChat» y lo cambia él).

| Para qué | Zernio | Alternativas |
|---|---|---|
| Publicar y programar | ✅ | Subir a mano (`manual`) o la herramienta que uses |
| DM automático por comentario | ✅ | ManyChat u otra (`manychat`, `otro`) |
| Métricas de tu cuenta | ✅ | Capturas del panel de Instagram |

## ManyChat

1. El agente te deja en `8-publicar/cola/<pieza>/pieza.md` la PALABRA (con variantes), el texto
   del DM y la respuesta al comentario.
2. En ManyChat, armá una automatización de comentarios de Instagram para ese post (o para
   cualquier post), con esas palabras clave y ese mensaje. Los nombres de los menús cambian
   seguido: si no lo encontrás, pedile al agente que lo busque en la ayuda de ManyChat.
3. Ojo: si tenés ManyChat y Zernio en la misma cuenta, las respuestas a historias las toma
   ManyChat. Elegí uno para cada cosa.

## Subir a mano

El agente te deja el archivo y el caption listo para pegar. Cuando lo subas, pasale el link para
que lo anote en `8-publicar/publicado.md`.

## Otro inbox (WhatsApp, mail, chat de tu web)

Si querés que la gente te escriba por otro lado, el CTA cambia: «Escribime "PALABRA" por WhatsApp
y te mando ___». El agente te prepara la respuesta para que la pegues o la cargues en tu
herramienta. Anotá en `config.json` qué usás.

## Reglas que valen para todos

- Instagram manda un solo DM automático por comentario: que sea el recurso.
- DM en texto plano: con botones, a quien no te sigue no le llega.
- Una palabra distinta por recurso.
