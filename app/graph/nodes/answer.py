def answer_node(state):

    state["answer"] = (
        f"Received: {state['user_message']}"
    )

    return state