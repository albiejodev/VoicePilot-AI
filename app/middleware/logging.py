import time
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.logger import logger
from app.core.metrics import (
    REQUEST_COUNT,
    REQUEST_LATENCY
)


class LoggingMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):

        start = time.time()

        REQUEST_COUNT.inc()

        response = await call_next(
            request
        )

        duration = (
            time.time() - start
        )

        REQUEST_LATENCY.observe(
            duration
        )

        logger.info(
            "request_completed",
            request_id=request.state.request_id,
            method=request.method,
            path=request.url.path,
            status_code=response.status_code,
            duration=duration
        )

        return response