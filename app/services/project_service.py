from datetime import UTC, datetime

from app.models.project import Project, ProjectStatus
from app.storage import projects


class ProjectService:
    def __init__(self) -> None:
        self._last_project_id = 0

    def create_project(self, description: str) -> Project:
        project = Project(
            id=self._next_project_id(),
            title=self._build_title(description),
            description=description,
            status=ProjectStatus.DRAFT,
            created_at=datetime.now(UTC),
            documents=[],
        )

        return projects.save(project)

    def list_projects(self) -> list[Project]:
        return projects.get_all()

    def get_project(self, project_id: int) -> Project | None:
        return projects.get(project_id)

    def _next_project_id(self) -> int:
        self._last_project_id += 1
        return self._last_project_id

    @staticmethod
    def _build_title(description: str) -> str:
        title = description.strip()
        return title[:40] if title else "Untitled project"


project_service = ProjectService()
