from fastapi import Request
from fastapi.responses import JSONResponse

from backend.src.exceptions.custom_exception import DisasterResponseException


async def disaster_exception_handler(
    request: Request,
    exc: DisasterResponseException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.message,
            "status_code": exc.status_code
        }
    )