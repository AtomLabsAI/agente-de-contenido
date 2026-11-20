# Instalar

Tiempo: 20 a 30 minutos la primera vez. Probado en Mac.

## 1. Claude

- Una cuenta de Claude con plan pago (Pro o más).
- Claude Code instalado: seguí las instrucciones de https://claude.com/claude-code.

## 2. Herramientas (Terminal)

Si no tenés Homebrew, instalalo con el comando de https://brew.sh. Después:

```bash
brew install yt-dlp ffmpeg whisper-cpp git
```

- `yt-dlp`: baja videos públicos para analizarlos.
- `ffmpeg`: corta y edita video.
- `whisper-cpp`: transcribe audio (el modelo se baja solo la primera vez que analizás un video).
- Google Chrome: lo usa para pasar las slides de los carruseles a PNG.

## 3. Esta carpeta

```bash
cd ~/Documents
git clone <link-del-repo> agente-de-contenido
cd agente-de-contenido
```

(Si te la pasaron como .zip, descomprimila en Documentos.)

## 4. Zernio (publicar, programar, DM automático y métricas)

1. Creá tu cuenta en https://zernio.com y conectá tu Instagram desde su panel. Tu Instagram tiene
   que ser **cuenta profesional** (creador o empresa).
2. Sumá Zernio a Claude Code (en la Terminal, fuera de Claude):
   ```bash
   claude mcp add --transport http zernio https://mcp.zernio.com/mcp
   ```
3. Abrí Claude Code en la carpeta, escribí `/mcp`, elegí **zernio** y entrá con tu cuenta.
4. Probalo: «Con Zernio, decime qué cuentas tengo conectadas y si están sanas».

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
