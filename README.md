# Agente de contenido · Atom Accelerator

Una carpeta que, abierta con Claude Code, se convierte en tu equipo de contenido:

- **Diagnostica tu cuenta** con Zernio y te dice en qué etapa estás y qué publicar.
- **Te saca ideas** de los videos que explotaron en tus competidores (outliers) y las adapta a tu nicho.
- **Edita tus reels** (cortes, títulos, subtítulos, animados) y **arma tus carruseles** con tu identidad.
- **Te escribe las historias** y, cuando tenés la cuenta lista, **el calendario de la semana**.
- **Publica y programa** con la automatización «comentá PALABRA → te mando el recurso». Nada sale sin tu ok.

## Las 3 etapas

| Etapa | Cuándo | Qué te recomienda |
|---|---|---|
| 1 · Ojos | Menos de 1.000 seguidores | Solo TOFU: reels y carruseles para conseguir ojos, sacados de outliers (3× la mediana o más) |
| 2 · Conexión | 1.000 o más, sostenido | Sigue el TOFU y suma historias: quién sos, qué hacés, tu día, nutrición |
| 3 · Sistema | 1.500 o más con vistas constantes | Calendario completo por días: TOFU + MOFU + BOFU e historias todos los días |

## Arrancar en 3 pasos

1. Instalá lo necesario: [docs/INSTALAR.md](docs/INSTALAR.md).
2. Abrí esta carpeta con Claude Code:
   ```bash
   cd ~/Documents/agente-de-contenido && claude
   ```
3. Escribí **«Arranquemos»**. El agente te pregunta quién sos, tus competidores y tu identidad,
   conecta Zernio y te dice en qué etapa estás.

## Qué hay adentro

| | |
|---|---|
| `CLAUDE.md` | El manual del agente: etapas, reglas y qué skill usa para cada pedido |
| `.claude/skills/` | `empezar` · `diagnostico` · `ideas` · `editar-videos` · `carruseles` · `historias` · `calendario` · `publicar` |
| `perfil/` | Tu perfil, competidores, referencias y el diagnóstico |
| `1-entrada/` … `8-publicar/` | Tus crudos, referencias, ideas, videos, carruseles, historias, recursos y lo que se publica |
| `docs/` | Cómo hacer todo: [GUIA](docs/GUIA.md) · [ETAPAS](docs/ETAPAS.md) · [CONECTORES](docs/CONECTORES.md) · [PEDIDOS](docs/PEDIDOS.md) |
| `scripts/` | `outliers.py`, `etapa.py`, `bajar.sh`, `analizar.sh` |
| `config.json` | Tus conectores y los números de las etapas y los outliers |
