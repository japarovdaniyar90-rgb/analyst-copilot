from datetime import datetime

from pydantic import BaseModel


class Document(BaseModel):
    id: int
    file_name: str
    extension: str
    mime_type: str | None
    size: int | None
    telegram_file_id: str
    uploaded_at: datetime
