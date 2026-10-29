# taskflow/api.py
from ninja import NinjaAPI

from accounts.auth import JWTAuth

DESCRIPTION = (
    "Track the tasks of your team's projects: members, labels, comments and attachments.\n\n"
    "Get a token from `POST /auth/token`, then click **Authorize** and paste it."
)

api = NinjaAPI(
    title="TaskFlow API",
    version="1.0",
    description=DESCRIPTION,
    urls_namespace="taskflow",
    auth=JWTAuth(),
)

api.add_router("/auth", "accounts.api.router")
api.add_router("/projects", "projects.api.router")
api.add_router("/projects/{project_id}/tasks", "tasks.api.router")
