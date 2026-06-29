from telegram import Update
from telegram.ext import ContextTypes

from app.bot.keyboards import MAIN_MENU_BUTTONS, NEW_PROJECT_BUTTON, main_menu_keyboard
from app.bot.states import UserState
from app.services.project_service import project_service


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None:
        return

    await update.message.reply_text(
        "👋 Привет, Данияр!\n\n"
        "Я AI SRS Assistant.\n\n"
        "Выберите действие:",
        reply_markup=main_menu_keyboard(),
    )


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None or context.user_data is None:
        return

    text = update.message.text or ""
    user_data = context.user_data

    if text == NEW_PROJECT_BUTTON:
        user_data["state"] = UserState.WAITING_PROJECT_DESCRIPTION
        await update.message.reply_text(
            "✍️ Опишите задачу одним сообщением.\n\n"
            "Например:\n"
            "Добавить смену номера телефона клиента."
        )
        return

    if text in MAIN_MENU_BUTTONS:
        user_data.pop("state", None)
        await _reply_feature_in_development(update)
        return

    if user_data.get("state") == UserState.WAITING_PROJECT_DESCRIPTION:
        project = project_service.create_project(text)
        user_data["state"] = UserState.PROJECT_CREATED

        await update.message.reply_text(
            f"✅ Проект создан\n\n"
            f"ID: {project.id}\n"
            f"Название: {project.title}\n"
            f"Статус: {project.status.value}"
        )
        return

    await _reply_feature_in_development(update)


async def _reply_feature_in_development(update: Update) -> None:
    await update.message.reply_text(
        "🚧 Эта функция пока находится в разработке."
    )
