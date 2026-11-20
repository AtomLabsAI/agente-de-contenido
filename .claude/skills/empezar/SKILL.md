---
name: empezar
description: Configura el agente de contenido la primera vez — pregunta quién es la persona, a quién le habla y su identidad, le pide competidores y videos de referencia, conecta Zernio (u otro canal) y corre el primer diagnóstico de la cuenta para saber en qué etapa está. Usar cuando digan "arranquemos", "configurá mi agente", "empecemos", o cuando perfil/perfil.md todavía tenga huecos (___).
---

# Empezar (configuración inicial)

El objetivo es dejar completos `perfil/perfil.md`, `perfil/competidores.md`, `config.json` y
`perfil/diagnostico.md`. Preguntá **de a un bloque por vez**, no todo junto. Si la persona no
sabe algo, dejalo como `___` y seguí: se completa después.

## 1. Quién sos (perfil.md · «Quién soy» y «A quién le hablo»)

Preguntá:
- Nombre, cuenta de Instagram y otras redes.
- Qué hace, en una línea, y qué vende (y a cuánto, si quiere decirlo).
- Su ángulo. Si vende IA o automatizaciones y no tiene uno, proponé **«IA para negocios»** o
  **«IA para pymes»** y chau: no hace falta un nicho más fino para arrancar.
- Seguidor ideal (a quién le habla el TOFU) y cliente ideal (a quién le vende). Explicá la
  diferencia en dos líneas: el TOFU le habla a mucha gente a la que le gusta el tema; dentro de
  esa gente está el cliente.
- Prueba social: clientes o casos que puede mostrar. **Si no tiene, queda vacío.** Nunca
  inventes.

## 2. Identidad (perfil.md · «Identidad»)

- Colores (hex) y tipografías. Si no tiene, ofrecé 2 o 3 paletas simples y que elija.
- Que deje 5 a 10 fotos suyas reales en `perfil/fotos/` (para portadas de carruseles).
- Cómo habla: voseo o tuteo, más formal o más directo. Si tiene un video o un texto suyo, pedilo
  y sacá el tono de ahí.

## 3. Referencias (perfil/referencias/ y competidores.md)

- **Competidores y referentes: mínimo 5 cuentas.** Pedí que priorice **referentes de EE. UU.**
  (van adelantados y no son su competencia directa). Las de habla hispana se pueden sumar, pero
  no como única fuente. Anotalas en `perfil/competidores.md`.
- **Videos y carruseles que le gustan:** 3 a 5 links. Son para copiar formato y estilo (cómo
  edita, qué títulos usa), no ideas. Bajalos con `scripts/bajar.sh` a `perfil/referencias/` y
  anotá al lado qué le gusta de cada uno.
- Si no conoce cuentas, sugerí que arme una **cuenta espía**: una cuenta de Instagram nueva que
  sigue solo cuentas del tema, así el feed se le llena de referencias.

## 4. Conectores (config.json · «conectores»)

Por defecto el agente viene con **Zernio** (publicar, programar, DM automático y métricas).
Preguntá cuál usa:

| Si usa | Qué hacés |
|---|---|
| Zernio | Verificá que el conector responda: `accounts_list` (plataforma instagram). Guardá el `account_id` en `config.json`. Si no está conectado, mandalo a `docs/INSTALAR.md` paso 4 |
| ManyChat u otra herramienta de DM | `dm_automatico: "manychat"`. Vos le preparás la palabra y el texto del DM; la automatización la arma él en su panel (`docs/CONECTORES.md`) |
| Nada / sube a mano | `publicar: "manual"`. Vos dejás todo listo en `8-publicar/cola/` y él sube |
| Mail, chat u otro inbox | `otro`. Preguntá cómo le llegan los mensajes y anotalo en `config.json` como texto. Adaptá el CTA (ej.: «escribime "PALABRA" por WhatsApp») |

Si `metricas` no es Zernio, para el diagnóstico pedile una captura de su panel de Instagram
(seguidores y vistas de los últimos 30 días) y de la pestaña Reels.

## 5. Diagnóstico

Corré la skill **`diagnostico`**. Al terminar, mostrale a la persona en 5 líneas:
- en qué etapa está y por qué (con sus números);
- qué tiene que hacer estas 2 semanas;
- el primer pedido que te puede hacer (ej.: «buscá outliers de @___ y dame 10 ideas»).

## Reglas

- No publiques ni conectes nada a nombre de la persona sin que lo pida.
- Claves y contraseñas: nunca las pidas por el chat. Los conectores se autentican en su propia
  ventana.
