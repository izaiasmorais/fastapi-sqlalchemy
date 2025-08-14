from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from typing import Dict

FIELD_MESSAGES: Dict[str, str] = {
    "name": "O nome é obrigatório",
    "email": "O email é obrigatório",
    "password": "A senha é obrigatória",
}

ERROR_TYPE_MESSAGES: Dict[str, Dict[str, str]] = {
    "name": {
        "string_too_short": "O nome deve ter pelo menos 2 caracteres",
        "missing": "O nome é obrigatório",
    },
    "email": {
        "value_error": "Digite um email válido",
        "missing": "O email é obrigatório",
    },
    "password": {
        "string_too_short": "A senha deve ter pelo menos 6 caracteres",
        "missing": "A senha é obrigatória",
    },
}


def get_error_message(field: str, error_type: str, input_value: any) -> str:
    if input_value == "" or input_value is None:
        return FIELD_MESSAGES.get(field, f"O campo {field} é obrigatório")

    field_errors = ERROR_TYPE_MESSAGES.get(field, {})
    return field_errors.get(error_type, f"Erro no campo {field}")


async def validation_exception_handler(_request: Request, exc: RequestValidationError):
    errors = []

    for error in exc.errors():
        field = error["loc"][-1] if error["loc"] else "unknown"
        error_type = error["type"]
        input_value = error.get("input")

        message = get_error_message(field, error_type, input_value)

        if message not in errors:
            errors.append(message)

    return JSONResponse(
        status_code=422, content={"success": False, "errors": errors, "data": None}
    )
