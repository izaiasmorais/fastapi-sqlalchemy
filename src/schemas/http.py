from pydantic import BaseModel
from typing import TypeVar, Generic, List, Optional

T = TypeVar("T")


class SuccessResponse(BaseModel, Generic[T]):
    success: bool = True
    errors: None = None
    data: Optional[T] = None


class ErrorResponse(BaseModel):
    success: bool = False
    errors: List[str]
    data: None = None
