
from ninja import NinjaAPI
from ninja.security import django_auth

from chat.api import router as rooms_router
from profiles.api import router as me_router

api = NinjaAPI(
    title="TaskFlow API",
    version="1.0",
    urls_namespace="library-api",
    description="API for managing projects and tasks.",
    auth=django_auth,
)

api.add_router("/rooms", rooms_router)
api.add_router("/me", me_router)

# locallibrary_config/api.py
from accounts.schemas import TokenOut
from accounts.tokens import create_token_pair


@api.post("/taskflow-token", response=TokenOut)
def taskflow_token(request):
    """Trade your login session for a TaskFlow token pair."""
    return create_token_pair(request.auth.id)
