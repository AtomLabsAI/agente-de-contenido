# Tu agente de contenido

**Un equipo de contenido entero adentro de una carpeta.** Lo abrís con Claude Code y se encarga
de todo tu Instagram: te dice qué publicar según cómo está tu cuenta, te saca ideas de los videos
que explotaron en tus competidores, te escribe los guiones, te edita los reels, te arma los
carruseles y los publica con la automatización «comentá PALABRA → te mando el recurso».

Vos hacés lo único que no se puede delegar: **grabar y aprobar.**

Es el mismo método con el que armamos @nacho.mirandap en Atom: después de un año publicando sin
resultados, cambiamos la forma de hacer contenido y llegamos a más de 30.000 seguidores. Nuestro
reel más visto, «Arma tu Jarvis en 7 pasos», pasó 1,5 millones de vistas. Las reglas de ese método
están adentro del agente.

Hecho por [Atom](https://atomlabsai.com) para los alumnos del Atom Accelerator.

---

## Lo que vas a tener al final

- **Un diagnóstico de tu cuenta** con números reales (Zernio): en qué etapa estás y qué te conviene
  publicar ahora. Nada de recetas genéricas.
- **Ideas validadas todas las semanas**, sacadas de los videos que hicieron 3 veces o más las
  vistas normales de tus 10 competidores, adaptadas a tu nicho.
- **Guiones listos para grabar**: gancho (con 2 alternativos), qué decir, qué va en pantalla y la
  PALABRA del llamado a la acción.
- **Tus reels editados solos**: tirás el crudo en una carpeta y un agente lo corta, le pone
  títulos y subtítulos, y lo revisa cuadro por cuadro antes de mostrártelo.
- **Carruseles con tu identidad**: tus colores, tus tipografías y tus fotos.
- **Animados** con HyperFrames o Remotion, y **trial reels** para probar ganchos con gente que
  todavía no te sigue.
- **Tu semana armada**: el agente te pregunta cuántas horas tenés y en qué horarios, y te dice qué
  hacer cada día.
- **Todo publicado** por Zernio con su DM automático. Nada sale sin tu ok.
- **Un tablero** que muestra en qué está cada pieza, de la idea a lo publicado.

## Cómo funciona

```
1. Conectás        Zernio (conector oficial de Claude) + tu Instagram
2. Le contás       quién sos, tus 10 competidores, tu identidad y cuánto tiempo tenés
3. Te audita       mira tu cuenta y te dice en qué etapa estás
4. Te arma         la semana: qué día hacés ideas, guiones, grabás, revisás y programás
5. Ideas           outliers de tus competidores + lo que te inspiró a vos → ideas para tu nicho
6. Guiones         uno por video, listos para leer
7. Grabás          vos, todo de corrido, y tirás los crudos en 1-entrada/
8. Edita           un agente por video, solo
9. Publica         con tu ok, programado para la semana que viene, con su DM automático
```

## Las 3 etapas: no publiques lo mismo con 300 seguidores que con 3.000

| Etapa | Cuándo | Qué te recomienda |
|---|---|---|
| **1 · Ojos** | De 0 a 1.000 seguidores | **Solo TOFU**: reels y carruseles para conseguir ojos. Vender con 10 seguidores no funciona: nadie responde |
| **2 · Conexión** | 1.000 a 1.500, sostenido | Sigue el TOFU, suma un video MOFU corto por semana y 2 o 3 historias por semana (la primera: quién sos y qué hacés) |
| **3 · Sistema** | 1.500 o más, con vistas constantes | El mix completo: TOFU + MOFU + BOFU, historias todos los días y la secuencia para pedir («Respondé PALABRA») |

El calendario va en las tres etapas: lo que cambia es qué entra en tu semana. Más detalle en
[docs/ETAPAS.md](docs/ETAPAS.md).

## Las skills (lo que sabe hacer)

| Skill | Qué hace | Le decís, por ejemplo |
|---|---|---|
| `empezar` | Te configura todo la primera vez | «Arranquemos» |
| `diagnostico` | Audita tu cuenta y te dice la etapa | «¿En qué etapa estoy?» |
| `ideas` | Outliers, análisis de videos, ideas y guiones | «Bajá este reel y analizalo: [link]» |
| `calendario` | Tu semana, con tus horarios | «Armame la semana» · «¿Qué me toca hoy?» |
| `editar-videos` | Reels, subtítulos, animados y variantes para trial | «Editame lo que está en 1-entrada» |
| `carruseles` | Carruseles con tu identidad | «Pasá este reel a carrusel» |
| `historias` | Qué subir en historias según tu etapa | «Armame la historia de quién soy» |
| `publicar` | Publica y programa con DM automático | «Programá la semana que viene» |

Y dos agentes que trabajan solos: `editor-de-reels` (uno por cada video que grabás) y
`carruseles` (uno por carrusel). Más pedidos para copiar y pegar en [docs/PEDIDOS.md](docs/PEDIDOS.md).

## El tablero

`TABLERO.html` es tu contenido en un solo lugar. Lo abrís con doble clic y ves:

> Ideas elegidas → Guiones para grabar → Crudos por editar → Editados para revisar → Listo para publicar → Publicado

Arriba, tu semana. El agente lo actualiza cada vez que avanza algo.

## Arrancar en 3 pasos

1. **Instalá lo necesario** (20 a 30 minutos, una sola vez): [docs/INSTALAR.md](docs/INSTALAR.md).
   Lo principal: Claude Code, unas herramientas para bajar y editar video, y **Zernio conectado
   desde el directorio oficial de conectores de Claude** (un clic, sin API).
2. **Bajá esta carpeta y abrila con Claude Code:**
   ```bash
   cd ~/Documents
   git clone https://github.com/AtomLabsAI/agente-de-contenido.git
   cd agente-de-contenido && claude
   ```
3. Escribí **«Arranquemos»**.

## Lo que no hace

- **No publica nada sin tu ok.** Ni una historia.
- **No inventa** números, clientes ni casos. Lo que no sabe, te lo pregunta.
- **No copia**: de cada referencia toma la idea y el formato, nunca el texto ni el video.
- **No usa tu sesión de Instagram** para bajar videos: solo videos públicos, y solo para analizarlos.

## Qué hay adentro

| | |
|---|---|
| `CLAUDE.md` | El manual del agente: etapas, reglas y qué skill usa para cada pedido |
| `.claude/skills/` | Las 8 skills |
| `.claude/agents/` | Los agentes de edición y de carruseles |
| `perfil/` | Tu perfil, competidores, referencias, fotos y el diagnóstico |
| `1-entrada/` … `8-publicar/` | Crudos, referencias, ideas y guiones, videos, carruseles, historias, recursos y lo que se publica |
| `docs/` | [GUIA](docs/GUIA.md) · [ETAPAS](docs/ETAPAS.md) · [INSTALAR](docs/INSTALAR.md) · [CONECTORES](docs/CONECTORES.md) · [PEDIDOS](docs/PEDIDOS.md) |
| `scripts/` | `outliers.py`, `etapa.py`, `bajar.sh`, `analizar.sh`, `tablero.py` |
| `config.json` | Tus conectores, tu tiempo y los números de las etapas y los outliers |

¿No usás Zernio? Funciona igual con ManyChat, subiendo a mano o con otro inbox:
[docs/CONECTORES.md](docs/CONECTORES.md).
