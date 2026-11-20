# Instalar

Tiempo: 20 a 30 minutos la primera vez. Probado en Mac.

## 1. Claude

- Una cuenta de Claude con plan pago (Pro o más).
- Claude Code instalado: seguí las instrucciones de https://claude.com/claude-code.

## 2. Herramientas (Terminal)

Si no tenés Homebrew, instalalo con el comando de https://brew.sh. Después:

```bash
brew install yt-dlp ffmpeg whisper-cpp git node
```

- `yt-dlp`: baja videos públicos para analizarlos.
- `ffmpeg`: corta y edita video.
- `whisper-cpp`: transcribe audio (el modelo se baja solo la primera vez que analizás un video).
- Google Chrome: lo usa para pasar las slides de los carruseles a PNG.
- `node` (versión 22 o más): para los videos animados con HyperFrames (`npx hyperframes`) o
  Remotion. Si no vas a hacer animados, podés saltearlo.

## 3. Esta carpeta

```bash
cd ~/Documents
git clone https://github.com/AtomLabsAI/agente-de-contenido.git
cd agente-de-contenido
```

(Si te la pasaron como .zip, descomprimila en Documentos.)

## 4. Zernio: el conector oficial de Claude (publicar, programar, DM automático y métricas)

Zernio está en el **directorio oficial de conectores de Claude**. Se conecta con un clic: sin API,
sin claves y sin comandos.

1. Creá tu cuenta en https://zernio.com y conectá tu Instagram desde su panel. Tu Instagram tiene
   que ser **cuenta profesional** (creador o empresa).
2. En **claude.ai** (o la app de escritorio de Claude): **Configuración → Conectores**, buscá
   **Zernio** y tocá **Conectar**. Entrá con tu cuenta de Zernio y aceptá.
3. Listo: el conector queda en tu cuenta de Claude y lo usa Claude Code, si entrás con la misma
   cuenta. Probalo dentro de la carpeta: «Con Zernio, decime qué cuentas tengo conectadas y si
   están sanas».

**Si en Claude Code no aparece:** escribí `/mcp` y fijate que figure Zernio. Si no está, como plan
B sumalo a mano desde la Terminal (fuera de Claude) y entrá con tu cuenta desde `/mcp`:

```bash
claude mcp add --transport http zernio https://mcp.zernio.com/mcp
```

¿No querés usar Zernio? Mirá [CONECTORES.md](CONECTORES.md): el agente funciona igual con
ManyChat, subiendo a mano o con otro inbox.

## 5. Arrancar

```bash
claude
```

y escribí **«Arranquemos»**.

## Si algo falla

| Problema | Arreglo |
|---|---|
| `command not found: yt-dlp` (o ffmpeg, whisper-cli) | Repetí el paso 2 |
| Zernio dice que la cuenta está desconectada | Reconectala en el panel de Zernio |
| Claude no ve las skills | Cerrá Claude Code y abrilo de nuevo **adentro de esta carpeta** |
