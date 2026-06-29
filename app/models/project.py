from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class ProjectStatus(str, Enum):
    DRAFT = "Draft"


class Project(BaseModel):
    id: int
    title: str
    description: str
    status: ProjectStatus
    created_at: datetime
    documents: list[str] = Field(default_factory=list)
