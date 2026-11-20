---
name: diagnostico
description: Analiza la cuenta de Instagram con Zernio (seguidores, vistas, qué rindió) y decide en qué etapa está — 1 Ojos (menos de 1.000, solo TOFU), 2 Conexión (1.000+, suma historias) o 3 Sistema (1.500+ con vistas constantes, calendario completo) — y qué tiene que publicar ahora. Usar cuando digan "diagnosticá mi cuenta", "¿en qué etapa estoy?", "¿qué subo esta semana?", "¿cómo vengo?", o una vez por mes.
---

# Diagnóstico de la cuenta

Escribe `perfil/diagnostico.md` (lo pisa entero) con la fecha de los datos.

## 1. Juntar los números

**Con Zernio** (`config.json` → `conectores.metricas = "zernio"`, cuenta en `cuenta.zernio_account_id`):
- Seguidores hoy y hace 14 y 30 días: `accounts_get_follower_stats`.
- Reels de los últimos 60 días con vistas, comentarios, guardados y fecha:
  `analytics_get_analytics` filtrado por la cuenta. Si trae trial reels (`isSharedToFeed: false`),
  separalos: se miden aparte.
- Si una herramienta no está en la lista, buscala con `search_tools` y llamala con `call_tool`.

**Sin Zernio:** pedile capturas del panel de Instagram (seguidores, cuentas alcanzadas 30 días) y
de la pestaña Reels. Leé los números de la captura; lo que no se lea es «sin dato».

## 2. Calcular

Pasá los datos a un JSON y corré:

```bash
python3 scripts/etapa.py --seguidores <hoy> --seguidores-hace-14 <n> --reels datos.json
```

`datos.json` es una lista `[{"fecha": "AAAA-MM-DD", "vistas": 1234}, ...]`. El script devuelve la
mediana de vistas por semana, si las vistas son constantes y la etapa según `config.json`.
Revisá el resultado: si algo no cierra (por ejemplo, una semana sin reels), decilo.

Además, a mano:
- Los 3 reels que mejor rindieron y los 3 peores: gancho, formato y etapa de cada uno.
- Cuántos reels por semana viene subiendo.

## 3. Escribir el diagnóstico

```markdown
# Diagnóstico · AAAA-MM-DD (datos de Zernio al AAAA-MM-DD)

## Etapa: N · Nombre
Por qué: ___ seguidores (hace 14 días: ___) · mediana de vistas por reel: ___ · vistas constantes: sí/no

## Lo que rindió
| Reel | Vistas | Gancho | Formato | Etapa |

## Lo que no rindió
| Reel | Vistas | Gancho | Qué cambiaría |

## Qué hacer ahora
- ...

## Próximo salto
Para pasar a la etapa ___ te falta: ___
```

## 4. Qué recomendar en cada etapa

**Etapa 1 · Ojos (menos de 1.000 seguidores)**
- **Solo TOFU.** Reels a cámara, b-roll, animados y carruseles que le hablan al seguidor ideal
  (gente a la que le gusta el tema), no al cliente.
- Las ideas salen de **outliers**: videos con 3× o más la mediana de su propia cuenta en los
  competidores (skill `ideas`). Los de 4× o más, primero.
- Nada de historias de venta ni de «comentá YO y te hago una auditoría»: con pocos seguidores no
  responde nadie.
- Volumen: lo que pueda sostener todas las semanas.

**Etapa 2 · Conexión (1.000 o más, sostenido 2 semanas)**
- El TOFU sigue siendo la base.
- Arrancan las historias (skill `historias`): primero una historia contando **quién es y qué
  hace**, después su día a día y algo de nutrición (una pregunta + 3 pasos a cámara).
- Algún reel o carrusel MOFU suelto: sobre conseguir clientes o un cambio de creencia del cliente.
- Señal para avanzar: la misma gente comenta seguido.

**Etapa 3 · Sistema (1.500 o más, con vistas constantes)**
- El calendario (skill `calendario`) pasa a tener TOFU + MOFU + BOFU.
- Historias todos los días con la semana tipo, y 1 o 2 días por semana la secuencia para pedir
  («Respondé PALABRA y te lo paso»).
- Casos de éxito cuando los haya.

En las tres etapas, después del diagnóstico corré (u ofrecé) la skill `calendario`: con la etapa
nueva cambia lo que entra en la semana.

Los umbrales están en `config.json` → `etapas`. Si la persona los cambió, usá los suyos.

## Reglas

- Siempre con la fecha de los datos.
- Nada inventado: si Zernio no trae un número, va «sin dato».
- Los trial reels se miden aparte de los reels del feed.
