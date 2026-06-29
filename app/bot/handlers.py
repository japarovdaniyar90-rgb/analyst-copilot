from telegram import Update
from telegram.ext import ContextTypes

from app.bot.keyboards import (
    MAIN_MENU_BUTTONS,
    MY_PROJECTS_BUTTON,
    NEW_PROJECT_BUTTON,
    main_menu_keyboard,
)
from app.bot.states import UserState
from app.models.project import Project
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

    if text == MY_PROJECTS_BUTTON:
        user_data.pop("state", None)
        projects = project_service.list_projects()
        await update.message.reply_text(_format_project_list(projects))
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


def _format_project_list(projects: list[Project]) -> str:
    if not projects:
        return (
            "📂 У вас пока нет проектов.\n\n"
            "Создайте первый проект с помощью кнопки:\n"
            "📝 Новый проект"
        )

    lines = ["📂 Мои проекты"]
    for index, project in enumerate(projects, start=1):
        lines.extend(
            [
                "",
                f"{_format_number(index)} {project.title}",
                f"{_status_icon(project.status.value)} {project.status.value}",
            ]
        )

    return "\n".join(lines)


def _format_number(number: int) -> str:
    numbers = {
        1: "1️⃣",
        2: "2️⃣",
        3: "3️⃣",
        4: "4️⃣",
        5: "5️⃣",
        6: "6️⃣",
        7: "7️⃣",
        8: "8️⃣",
        9: "9️⃣",
        10: "🔟",
    }
    return numbers.get(number, f"{number}.")


def _status_icon(status: str) -> str:
    icons = {
        "Draft": "🟡",
        "Interview": "🟢",
    }
    return icons.get(status, "⚪")
