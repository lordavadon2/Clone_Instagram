from fastapi import APIRouter

from src.app.user.router import router as user_router
from src.app.auth.router import router as auth_router
from src.app.posts.router import router as post_router
from src.app.comments.router import router as comment_router

api_router = APIRouter()

api_router.include_router(auth_router, tags=['Auth'], prefix="/auth")
api_router.include_router(user_router, tags=['User'], prefix="/users")
api_router.include_router(post_router, tags=['Post'], prefix="/posts")
api_router.include_router(comment_router, tags=['Comment'], prefix="/comments")
