from langchain.tools import tool
from src.rag import retriever

@tool
def calculator(expression: str):
    """Perform calculations"""
    return str(eval(expression))

@tool
def rag_search(query: str):
    """Search knowledge base"""

    docs = retriever.get_relevant_documents(query)

    return "\n".join(
        [doc.page_content for doc in docs]
    )