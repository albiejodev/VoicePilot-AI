class SessionService:

    def __init__(self):
        self.sessions = {}

    def create_session(
        self,
        session_id
    ):
        self.sessions[session_id] = {
            "messages": []
        }

    def add_message(
        self,
        session_id,
        message
    ):
        self.sessions[session_id][
            "messages"
        ].append(message)

    def get_session(
        self,
        session_id
    ):
        return self.sessions.get(
            session_id
        )