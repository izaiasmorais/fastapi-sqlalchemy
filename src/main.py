from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.exceptions import RequestValidationError
from src.database import init_db, close_db
from src.controllers.auth import router as auth_router
from scalar_fastapi import get_scalar_api_reference
from src.utils.error_handler import validation_exception_handler

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()


app = FastAPI(
    title="FastAPI Clean",
    description="API auto-documentável com FastAPI, Pydantic e SQLAlchemy",
    version="1.0.0",
    lifespan=lifespan,
    docs_url=None,
    redoc_url=None,
)


@app.get("/", include_in_schema=False)
async def root():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )


@app.get("/docs", include_in_schema=False)
async def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )


app.add_exception_handler(RequestValidationError, validation_exception_handler)


@app.get(
    "/health",
    tags=["Health"],
    summary="Health Check",
    description="Endpoint para verificar se a API está funcionando corretamente",
)
async def health():
    return {"message": "FastAPI Auth API"}


app.include_router(auth_router)
