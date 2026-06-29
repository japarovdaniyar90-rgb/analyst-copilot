from telegram import (
    Update,
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from config import Config
from state import users


MAIN_MENU = [
    ["📝 Новый проект"],
    ["📄 Проверить документ"],
    ["📊 Диаграммы"],
    ["⚙️ Настройки", "❓ Помощь"],
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = ReplyKeyboardMarkup(
        MAIN_MENU,
        resize_keyboard=True,
    )

    await update.message.reply_text(
        "👋 Привет, Данияр!\n\n"
        "Я AI SRS Assistant.\n\n"
        "Выберите действие:",
        reply_markup=keyboard,
    )


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text
    user_id = update.effective_user.id

    # Создание нового проекта
    if text == "📝 Новый проект":

        users[user_id] = {
            "state": "waiting_description"
        }

        await update.message.reply_text(
            "✍️ Опишите задачу одним сообщением.\n\n"
            "Например:\n"
            "Добавить смену номера телефона клиента."
        )
        return

    # Ожидаем описание
    if (
        user_id in users
        and users[user_id]["state"] == "waiting_description"
    ):

        users[user_id]["description"] = text
        users[user_id]["state"] = "created"

        await update.message.reply_text(
            f"✅ Проект создан!\n\n"
            f"Описание:\n{text}"
        )

        return

    # Пока остальные кнопки не реализованы
    await update.message.reply_text(
        "🚧 Эта функция пока находится в разработке."
    )


def main():

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

    print("✅ Bot started")

    app.run_polling()


if __name__ == "__main__":
    main()