from app.models.document import Document
from app.models.project import Project


def format_project_list(projects: list[Project]) -> str:
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


def format_project_workspace(project: Project) -> str:
    return (
        f"📁 {project.title}\n\n"
        f"Статус: {project.status.value}\n"
        f"Документов: {len(project.documents)}\n\n"
        "Выберите действие:"
    )


def format_document_upload_success(
    document: Document,
    documents_count: int,
) -> str:
    return (
        "✅ Документ успешно загружен.\n\n"
        f"Имя файла: {document.file_name}\n"
        f"Тип файла: {document.extension.upper()}\n"
        f"Документов в проекте: {documents_count}"
    )


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
