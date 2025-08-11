from fastapi import APIRouter
from . import users, documents, reminders

router = APIRouter()

router.include_router(users.router, tags=["Users"])
router.include_router(documents.router, tags=["Documents"])
router.include_router(reminders.router, tags=["Reminders"])
