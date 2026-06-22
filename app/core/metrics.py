from prometheus_client import (Counter,Histogram,Gauge)

#http metrics

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total requests"
)


REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Request latency"
)



#websocket metrics 

ACTIVE_CONNECTIONS = Gauge(
    "active_websocket_connections",
    "Current active websocket connections"
)


MESSAGES_RECEIVED = Counter(
    "websocket_messages_received_total",
    "Total websocket messages received"
)

MESSAGES_SENT = Counter(
    "websocket_messages_sent_total",
    "Total websocket messages sent"
)


#langgraph metrics 

GRAPH_EXECUTIONS = Counter(
    "graph_executions_total",
    "LangGraph executions"
)


GRAPH_EXECUTION_TIME = Histogram(
    "graph_execution_duration_seconds",
    "Time taken for LangGraph execution"
)
