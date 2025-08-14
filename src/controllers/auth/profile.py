from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.user import User
from src.schemas.user import UserProfile
from src.schemas.http import ErrorResponse, SuccessResponse
from src.utils.auth import get_current_user
from src.database import get_db

router = APIRouter()


@router.get(
    "/profile",
    response_model=SuccessResponse[UserProfile],
    responses={401: {"model": ErrorResponse, "description": "Unauthorized"}},
)
async def get_profile(
    current_user_id: int = Depends(get_current_user), db: AsyncSession = Depends(get_db)
):
    # Buscar usuário pelo ID
    stmt = select(User).where(User.id == current_user_id)
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=404, detail=ErrorResponse(errors=["Usuário não encontrado"])
        )

    user_data = UserProfile(name=user.name, email=user.email)
    return SuccessResponse[UserProfile](data=user_data)
