from app.services.redis_service import (
    health_check
)

from app.core.logger import logger



def validate_services():

    if not health_check():

        raise Exception(
            "Redis unavailable"
        )

    logger.info(
        "redis_connection_success"
    )