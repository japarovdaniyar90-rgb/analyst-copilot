projects = {}

last_project_id = 0


def create_project(description: str):

    global last_project_id

    last_project_id += 1

    project = {
        "id": last_project_id,
        "title": description[:40],
        "description": description,
        "status": "Draft",
        "documents": [],
    }

    projects[last_project_id] = project

    return project


def get_projects():

    return list(projects.values())