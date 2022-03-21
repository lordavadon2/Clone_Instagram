from fastapi import APIRouter

from src.app.user.router import router as user_router
from src.app.auth.router import router as auth_router

api_router = APIRouter()

api_router.include_router(auth_router, tags=['Auth'], prefix="/auth")
api_router.include_router(user_router, tags=['User'], prefix="/user")
