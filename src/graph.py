from typing import TypedDict
from langgraph.graph import StateGraph

from src.agent import generate_response

class AgentState(TypedDict):
    user_input: str
    response: str

def chatbot(state):

    answer = generate_response(
        state["user_input"]
    )

    return {
        "response": answer
    }

graph = StateGraph(AgentState)

graph.add_node(
    "chatbot",
    chatbot
)

graph.set_entry_point(
    "chatbot"
)

graph.set_finish_point(
    "chatbot"
)

app = graph.compile()