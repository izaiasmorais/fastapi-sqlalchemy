from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.user import User
from src.schemas.auth import SignInRequest, TokenResponse
from src.schemas.http import ErrorResponse, SuccessResponse
from src.utils.auth import verify_password, create_access_token
from src.database import get_db

router = APIRouter()


@router.post(
    "/sign-in",
    response_model=SuccessResponse[TokenResponse],
    responses={401: {"model": ErrorResponse, "description": "Invalid credentials"}},
)
async def sign_in(request: SignInRequest, db: AsyncSession = Depends(get_db)):
    # Buscar usuário pelo email
    stmt = select(User).where(User.email == request.email.lower())
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user or not verify_password(request.password, user.password):
        raise HTTPException(
            status_code=401, detail=ErrorResponse(errors=["Email ou senha incorretos"])
        )

    access_token = create_access_token(data={"sub": str(user.id)})
    token_data = TokenResponse(access_token=access_token)
    return SuccessResponse[TokenResponse](data=token_data)
