from telegram import Update
from telegram.ext import ContextTypes

from app.bot.formatters import format_document_upload_success
from app.bot.states import UserState
from app.services.document_service import (
    ActiveProjectNotFoundError,
    UnsupportedDocumentFormatError,
    document_service,
)


async def document_message(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    if update.message is None or context.user_data is None:
        return

    telegram_document = update.message.document
    if telegram_document is None:
        return

    if context.user_data.get("state") != UserState.WAITING_DOCUMENT_UPLOAD:
        await update.message.reply_text(
            "❌ Сначала выберите проект."
        )
        return

    project_id = context.user_data.get("active_project_id")
    if not isinstance(project_id, int):
        context.user_data.pop("state", None)
        await update.message.reply_text(
            "❌ Сначала выберите проект."
        )
        return

    file_name = telegram_document.file_name or "document"
    try:
        document = document_service.upload_document(
            project_id=project_id,
            file_name=file_name,
            mime_type=telegram_document.mime_type,
            size=telegram_document.file_size,
            telegram_file_id=telegram_document.file_id,
        )
    except UnsupportedDocumentFormatError:
        await update.message.reply_text(
            "❌ Данный формат пока не поддерживается."
        )
        return
    except ActiveProjectNotFoundError:
        context.user_data.pop("state", None)
        await update.message.reply_text(
            "❌ Сначала выберите проект."
        )
        return

    context.user_data.pop("state", None)
    documents_count = len(document_service.list_documents(project_id))
    await update.message.reply_text(
        format_document_upload_success(document, documents_count)
    )
