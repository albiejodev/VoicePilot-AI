from fastapi import Request
from fastapi.responses import JSONResponse

from app.core.logger import logger



async def global_exception_handler(
    request: Request,
    exc: Exception
):

    logger.error(
        "unhandled_exception",
        request_id=request.state.request_id,
        error=str(exc)
    )

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message":
            "Internal Server Error"
        }
    )