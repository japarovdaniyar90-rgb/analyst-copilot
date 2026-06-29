from enum import Enum


class UserState(str, Enum):
    WAITING_PROJECT_DESCRIPTION = "waiting_project_description"
    WAITING_DOCUMENT_UPLOAD = "waiting_document_upload"
    PROJECT_CREATED = "project_created"
