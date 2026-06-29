from telegram import ReplyKeyboardMarkup


NEW_PROJECT_BUTTON = "📝 Новый проект"

MAIN_MENU = [
    [NEW_PROJECT_BUTTON],
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
