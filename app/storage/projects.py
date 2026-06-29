from app.models.project import Project


_projects: dict[int, Project] = {}


def save(project: Project) -> Project:
    _projects[project.id] = project
    return project


def get(project_id: int) -> Project | None:
    return _projects.get(project_id)


def get_all() -> list[Project]:
    return list(_projects.values())


def delete(project_id: int) -> bool:
    return _projects.pop(project_id, None) is not None
