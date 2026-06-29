from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from app.models.project import Project


NEW_PROJECT_BUTTON = "📝 Новый проект"
MY_PROJECTS_BUTTON = "📂 Мои проекты"

CALLBACK_PROJECT_OPEN = "project:open:"
CALLBACK_WORKSPACE_ACTION = "workspace:action:"

WORKSPACE_UPLOAD_BRD = "upload_brd"
WORKSPACE_AI_ANALYSIS = "ai_analysis"
WORKSPACE_REQUIREMENTS = "requirements"
WORKSPACE_DIAGRAMS = "diagrams"
WORKSPACE_SETTINGS = "settings"

WORKSPACE_ACTIONS = [
    ("📄 Загрузить BRD", WORKSPACE_UPLOAD_BRD),
    ("🧠 AI Анализ", WORKSPACE_AI_ANALYSIS),
    ("📝 Требования", WORKSPACE_REQUIREMENTS),
    ("📊 Диаграммы", WORKSPACE_DIAGRAMS),
    ("⚙️ Настройки проекта", WORKSPACE_SETTINGS),
]

MAIN_MENU = [
    [NEW_PROJECT_BUTTON],
    [MY_PROJECTS_BUTTON],
    ["📄 Проверить документ"],
    ["📊 Диаграммы"],
    ["⚙️ Настройки", "❓ Помощь"],
]

MAIN_MENU_BUTTONS = {
    button
    for row in MAIN_MENU
    for button in row
}


def main_menu_keyboard() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        MAIN_MENU,
        resize_keyboard=True,
    )


def project_selection_keyboard(projects: list[Project]) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    project.title,
                    callback_data=f"{CALLBACK_PROJECT_OPEN}{project.id}",
                )
            ]
            for project in projects
        ]
    )


def project_workspace_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    label,
                    callback_data=f"{CALLBACK_WORKSPACE_ACTION}{action}",
                )
            ]
            for label, action in WORKSPACE_ACTIONS
        ]
    )
