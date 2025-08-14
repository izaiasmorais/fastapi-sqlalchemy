from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from src.models.user import User
from src.schemas.auth import SignUpRequest
from src.schemas.http import ErrorResponse, SuccessResponse
from src.utils.auth import hash_password
from src.database import get_db

router = APIRouter()


@router.post(
    "/sign-up",
    status_code=201,
    response_model=SuccessResponse[None],
    responses={409: {"model": ErrorResponse, "description": "Email já cadastrado"}},
)
async def sign_up(request: SignUpRequest, db: AsyncSession = Depends(get_db)):

    stmt = select(User).where(User.email == request.email.lower())
    result = await db.execute(stmt)
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=409, detail=ErrorResponse(errors=["Email já cadastrado"])
        )

    new_user = User(
        name=request.name,
        email=request.email.lower(),
        password=hash_password(request.password),
    )

    db.add(new_user)
    await db.commit()

    return SuccessResponse()
