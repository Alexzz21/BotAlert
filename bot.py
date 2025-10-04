import os
from telegram.ext import Application, CommandHandler

# Leer el token desde variable de entorno
TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("¡Hola! Soy tu bot corriendo en Dokploy 🚀")

def main():
    if not TOKEN:
        raise ValueError("❌ No se encontró la variable de entorno BOT_TOKEN")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
