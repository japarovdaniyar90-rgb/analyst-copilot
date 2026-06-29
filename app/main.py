from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
)

from app.bot.handlers import message, start
from app.config import Config


def main() -> None:
    token = Config.TELEGRAM_TOKEN

    if not token:
        raise ValueError("TELEGRAM_TOKEN не найден в .env")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message,
        )
    )

    print("Bot started")
    app.run_polling()


if __name__ == "__main__":
    main()
