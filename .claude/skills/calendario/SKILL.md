---
name: calendario
description: Arma solo el calendario de contenido de la semana que viene según el tiempo de la persona (horas por semana, días y horarios) y la etapa de su cuenta — qué día hace ideas, guiones, grabar, revisar y programar, y qué se publica cada día (en la etapa 1 solo TOFU, en la 2 suma historias, en la 3 el mix completo). Usar cuando digan "armame el calendario", "planificá la semana", "qué hago cada día", "organizame el contenido", al terminar la skill empezar, y al arrancar una sesión si la semana que viene no tiene calendario.
---

# Calendario de contenido

El calendario lo armás vos, no la persona. Ella te dio su tiempo; vos le decís qué hacer cada día
y qué sale publicado cada día. Va a `8-publicar/calendario.md`: una sección por semana, la más
nueva arriba.

Antes de arrancar leé:
- `perfil/perfil.md` («Mi tiempo») y `config.json` → `disponibilidad` y `tiempos_por_pieza_min`.
  Si no hay horas por semana o días, preguntalos (sección 3 de la skill `empezar`) antes de seguir.
- La etapa en `perfil/diagnostico.md`.
- `3-ideas/ideas.md` (qué ideas hay marcadas) y `8-publicar/publicado.md` (qué salió la semana pasada).

## 1. Cuánto entra en la semana

Con las horas que dio y los tiempos de `config.json`:

```
minutos libres = horas_por_semana × 60
fijo = ideas_por_semana + programar_por_semana (+ historias_por_dia × días de historias, si la etapa tiene historias)
por reel = guion + grabar + revisar_edicion
reels = (minutos libres − fijo − carruseles × carrusel) ÷ por reel, redondeado para abajo
```

- Arrancá con más reels que carruseles: en la etapa 1 los reels traen los ojos. Si sobra tiempo,
  sumá carruseles (salen de reels que ya rindieron).
- **Mejor poco y todas las semanas que mucho una semana y nada la siguiente.** Si el número da
  alto, proponé algo un poco por debajo para que lo sostenga.
- Decile la cuenta en una línea: «Con 4 horas te entran 5 reels y 2 carruseles».
- Los tiempos de `config.json` son una estimación inicial. Al cerrar cada semana preguntale cuánto
  tardó de verdad en grabar y en guionar, y actualizalos.

## 2. Repartir la producción en sus días

La regla: **un tipo de tarea por día y una semana de ventaja**. Lo que se produce esta semana sale
la semana que viene. Nunca grabar, editar y publicar el mismo día: si un paso se traba, ese día no
sale nada.

| Tarea | Qué hace la persona | Qué hacés vos |
|---|---|---|
| Ideas | Te pasa capturas de los competidores y elige ideas | Skill `ideas`: outliers e ideas para su etapa |
| Guiones | Revisa y ajusta | Skill `ideas`, sección 6 |
| Grabar | Graba todo de corrido y tira los crudos en `1-entrada/` | Hoja de grabación: los guiones en orden, solo el texto, la PALABRA marcada |
| Revisar | Mira cada reel y pide cambios | Skill `editar-videos` (editás antes de ese día) |
| Programar | Da el ok a la lista | Skill `publicar`: fecha, caption, palabra y DM, y espera el ok |

Según cuántos días tiene:
- **5 o más días:** una tarea por día, en el orden de la tabla.
- **3 o 4 días:** día 1 ideas + guiones · día 2 grabar · día 3 revisar + programar (y el 4.º, si
  hay, para carruseles o historias).
- **1 o 2 días:** día 1 ideas + guiones · día 2 grabar. La revisión y la programación las hace en
  15 minutos otro día, desde el celular.

Poné cada tarea en el bloque horario que dio, con su duración estimada.

## 3. Qué se publica cada día (según la etapa)

| Etapa | Feed | Historias |
|---|---|---|
| 1 · Ojos | **Solo TOFU**: los reels y carruseles que entraron, repartidos en la semana | No (o su día a día, sin pedir nada) |
| 2 · Conexión | TOFU de base + 1 MOFU por semana si hay tiempo | 3 o 4 días: primero «quién soy y qué hago», después conexión y nutrición (skill `historias`) |
| 3 · Sistema | TOFU + MOFU + BOFU. Proponé el reparto según lo que rindió y preguntale si le cierra | Todos los días con la semana tipo, 1 o 2 días la secuencia para pedir (skill `historias`) |

- Cada pieza con su etapa, su gancho (o «idea pendiente» si todavía no está) y su PALABRA.
- Hora de publicar: la de `disponibilidad.hora_de_publicar` o la que saque el diagnóstico.
- Nuestra meta en @nacho.mirandap es 7 reels y 7 carruseles por semana, con historias los 7 días.
  Para alguien que arranca, lo que entre en su tiempo.

## 4. El archivo

```markdown
## Semana del AAAA-MM-DD (etapa N · nombre)

Tu tiempo: ___ h · Te entran: ___ reels y ___ carruseles

### Producción (esta semana)
| Día y hora | Tarea | Duración | Qué te llevás |
|---|---|---|---|
| Mar 19-20:30 | Ideas + guiones | 1 h 30 | ___ guiones listos |

### Publicación (semana que viene)
| Día | Hora | Feed | Etapa | Gancho | PALABRA | Historias |
|---|---|---|---|---|---|---|
| Lun | 19:00 | Reel | TOFU | «___» | ___ | — |
```

Mostrale la semana, preguntale si le cierra y ajustá. Cuando la aprueba, guardala.

## 5. Todas las semanas

- Al arrancar una sesión, si la semana que viene no tiene calendario, ofrecé armarlo.
- Al cerrar la semana: qué se publicó de lo planificado, qué no y por qué, cuánto tardó de verdad
  (para los tiempos), y qué rindió (diagnóstico corto con Zernio).
- Si la etapa cambió, el calendario cambia con ella: avisale qué se suma.

## Checklist del día de grabación (para pasarle)

- [ ] Guiones en orden, en la hoja de grabación
- [ ] Micrófono puesto y probado
- [ ] Aire arriba y abajo del encuadre: Instagram tapa esas zonas
- [ ] Arranca con el gancho, sin «hola». El paso 1 en el segundo 2
- [ ] Si se equivoca, repite la frase entera: la edición se queda con la última toma limpia
- [ ] Dice la PALABRA del CTA dos veces
- [ ] Un lugar de la casa para los TOFU y otro para los MOFU
- [ ] Al terminar, los crudos a `1-entrada/` con el nombre del guion
