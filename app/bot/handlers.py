from telegram import Update
from telegram.ext import ContextTypes

from app.bot.keyboards import (
    CALLBACK_PROJECT_OPEN,
    CALLBACK_WORKSPACE_ACTION,
    MAIN_MENU_BUTTONS,
    MY_PROJECTS_BUTTON,
    NEW_PROJECT_BUTTON,
    main_menu_keyboard,
    project_selection_keyboard,
    project_workspace_keyboard,
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
        await update.message.reply_text(
            _format_project_list(projects),
            reply_markup=project_selection_keyboard(projects) if projects else None,
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


async def callback_query(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    query = update.callback_query
    if query is None or context.user_data is None:
        return

    await query.answer()

    data = query.data or ""
    if data.startswith(CALLBACK_PROJECT_OPEN):
        await _handle_project_open_callback(update, context, data)
        return

    if data.startswith(CALLBACK_WORKSPACE_ACTION):
        await _handle_workspace_action_callback(update)
        return

    if query.message is not None:
        await query.message.reply_text("Неизвестное действие.")


async def _handle_project_open_callback(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    data: str,
) -> None:
    query = update.callback_query
    if query is None or query.message is None or context.user_data is None:
        return

    project_id = _parse_callback_project_id(data)
    if project_id is None:
        await query.message.reply_text("Проект не найден.")
        return

    project = project_service.get_project(project_id)
    if project is None:
        await query.message.reply_text("Проект не найден.")
        return

    context.user_data["active_project_id"] = project.id
    await query.edit_message_text(
        _format_project_workspace(project),
        reply_markup=project_workspace_keyboard(),
    )


async def _handle_workspace_action_callback(update: Update) -> None:
    query = update.callback_query
    if query is None or query.message is None:
        return

    await query.message.reply_text(
        "🚧 Функция находится в разработке."
    )


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


def _format_project_workspace(project: Project) -> str:
    return (
        f"📁 {project.title}\n\n"
        f"Статус: {project.status.value}\n"
        f"Документов: {len(project.documents)}\n\n"
        "Выберите действие:"
    )


def _parse_callback_project_id(data: str) -> int | None:
    project_id = data.removeprefix(CALLBACK_PROJECT_OPEN)
    if not project_id.isdigit():
        return None

    return int(project_id)
