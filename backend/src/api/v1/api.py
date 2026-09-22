from fastapi import APIRouter
from backend.src.api.v1.routes.home import router as home_router


api_router = APIRouter()


api_router.include_router(
    home_router,
    tags=["Home"]
)