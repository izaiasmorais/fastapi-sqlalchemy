from pydantic import BaseModel, EmailStr, Field


class SignUpRequest(BaseModel):
    name: str = Field(min_length=2, max_length=100, description="Nome do usuário", )
    email: EmailStr = Field(description="Email do usuário")
    password: str = Field(min_length=6, description="Senha do usuário")


class SignInRequest(BaseModel):
    email: EmailStr = Field(description="Email do usuário")
    password: str = Field(min_length=6, description="Senha do usuário")


class TokenResponse(BaseModel):
    access_token: str = Field(description="Token de acesso")
    token_type: str = Field(description="Tipo de token", default="bearer")
