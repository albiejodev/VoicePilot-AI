from fastapi import (APIRouter,WebSocket,WebSocketDisconnect)
from app.core.logger import logger
from app.graph.workflow import graph
import time
from app.services.connection_manager import manager
from app.core.metrics import (
    GRAPH_EXECUTIONS,
    GRAPH_EXECUTION_TIME,
    MESSAGES_RECEIVED,
    MESSAGES_SENT
)


router = APIRouter()


@router.websocket("/ws/{session_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    session_id:str
):
    await manager.connect(
        session_id,
        websocket
    )

    try:

        while True:

            message = await websocket.receive_text()

            logger.info(
            "message_received",
            session_id=session_id,
            message_length=len(message)
            )

            MESSAGES_RECEIVED.inc()

            start_time = time.time()

            GRAPH_EXECUTIONS.inc()

            result = graph.invoke(
                {
                    "session_id":session_id,
                    "user_message":message,
                    "answer":""
                }
            )

            execution_time = (
                time.time() - start_time
            )

            GRAPH_EXECUTION_TIME.observe(
                execution_time
            )

            await manager.send_message(
                session_id,
                result
            )

            MESSAGES_SENT.inc()

            logger.info(
                "message_sent",
                session_id=session_id,
                execution_time=execution_time
            )



    except Exception as e:

        logger.error(
            "websocket_error",
            session_id=session_id,
            error=str(e)
        )

        manager.disconnect(session_id)

        logger.info(
            "client_disconnected",
            session_id=session_id
        )
