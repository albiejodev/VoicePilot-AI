from typing import TypedDict

class AgentState(TypedDict):
    session_id: str
    user_message: str
    answer: str