from enum import Enum


class UserState(str, Enum):
    WAITING_PROJECT_DESCRIPTION = "waiting_project_description"
    PROJECT_CREATED = "project_created"
