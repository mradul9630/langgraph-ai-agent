from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from src.memory import chat_history

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3
)

def generate_response(query):

    chat_history.append(f"User: {query}")

    prompt = "\n".join(chat_history)

    response = llm.invoke(prompt)

    chat_history.append(
        f"Assistant: {response.content}"
    )

    return response.content