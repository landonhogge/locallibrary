from ninja import NinjaAPI
from chat.api import router as rooms_router

api = NinjaAPI(
    title="TaskFlow API",
    version="1.0",
    description="API for managing projects and tasks.",
)

api.add_router("/rooms", rooms_router)