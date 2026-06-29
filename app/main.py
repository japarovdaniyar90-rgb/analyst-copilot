import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

load_dotenv()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет, Данияр!\n\n"
        "Я AI SRS Assistant.\n\n"
        "Пока я умею только здороваться 🙂\n\n"
        "Версия: 0.1"
    )


def main():
    token = os.getenv("TELEGRAM_TOKEN")

    if not token:
        raise ValueError("TELEGRAM_TOKEN не найден в .env")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Bot started")

    app.run_polling()


if __name__ == "__main__":
    main()