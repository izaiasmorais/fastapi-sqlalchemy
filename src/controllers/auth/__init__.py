from fastapi import APIRouter
from .sign_up import router as sign_up_router
from .sign_in import router as sign_in_router
from .profile import router as profile_router


router = APIRouter(prefix="/auth", tags=["Auth"])

router.include_router(sign_up_router)
router.include_router(sign_in_router)
router.include_router(profile_router)
