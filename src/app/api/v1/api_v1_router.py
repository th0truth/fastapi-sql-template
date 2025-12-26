from fastapi import APIRouter
from routes import (
  user
)

# Initialize v1 router
api_v1_router = APIRouter()

# Included routers
api_v1_router.include_router(user.router, prefix="/user")