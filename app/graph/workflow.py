from langgraph.graph import StateGraph

from app.graph.state import AgentState

from app.graph.nodes.memory import memory_node
from app.graph.nodes.router import router_node
from app.graph.nodes.answer import answer_node




builder = StateGraph(AgentState)

builder.add_node(
    "memory",
    memory_node
)

builder.add_node(
    "router",
    router_node
)

builder.add_node(
    "answer",
    answer_node
)

builder.add_edge(
    "memory",
    "router"
)

builder.add_edge(
    "router",
    "answer"
)

builder.set_entry_point("memory")

graph = builder.compile()