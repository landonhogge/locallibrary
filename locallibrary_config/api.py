
from ninja import NinjaAPI
from ninja.security import django_auth

from chat.api import router as rooms_router

api = NinjaAPI(
    title="TaskFlow API",
    version="1.0",
    urls_namespace="library-api",
    description="API for managing projects and tasks.",
    auth=django_auth,
)

api.add_router("/rooms", rooms_router)
