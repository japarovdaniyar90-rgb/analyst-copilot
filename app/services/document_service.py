from datetime import UTC, datetime
from pathlib import Path

from app.models.document import Document
from app.storage import projects


SUPPORTED_EXTENSIONS = {"pdf", "docx", "txt", "md"}


class UnsupportedDocumentFormatError(ValueError):
    pass


class ActiveProjectNotFoundError(ValueError):
    pass


class DocumentService:
    def __init__(self) -> None:
        self._last_document_id = 0

    def upload_document(
        self,
        project_id: int,
        file_name: str,
        mime_type: str | None,
        size: int | None,
        telegram_file_id: str,
    ) -> Document:
        extension = self._get_extension(file_name)
        if extension not in SUPPORTED_EXTENSIONS:
            raise UnsupportedDocumentFormatError

        project = projects.get(project_id)
        if project is None:
            raise ActiveProjectNotFoundError

        document = Document(
            id=self._next_document_id(),
            file_name=file_name,
            extension=extension,
            mime_type=mime_type,
            size=size,
            telegram_file_id=telegram_file_id,
            uploaded_at=datetime.now(UTC),
        )

        project.documents.append(document)
        projects.save(project)
        return document

    def list_documents(self, project_id: int) -> list[Document]:
        project = projects.get(project_id)
        if project is None:
            return []

        return project.documents

    def _next_document_id(self) -> int:
        self._last_document_id += 1
        return self._last_document_id

    @staticmethod
    def _get_extension(file_name: str) -> str:
        return Path(file_name).suffix.removeprefix(".").lower()


document_service = DocumentService()
