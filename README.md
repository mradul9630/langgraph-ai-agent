# LangGraph AI Agent

A stateful AI Agent built using LangGraph, LangChain, and Google's Gemini API. The project demonstrates conversational memory, workflow orchestration, and agent-based application development using modern Generative AI technologies.

## Features

* Conversational AI powered by Gemini
* Stateful workflow management using LangGraph
* Conversation memory for context-aware interactions
* Modular project structure
* Easy integration with external tools and APIs
* Foundation for RAG, tool calling, and multi-step reasoning workflows

## Tech Stack

* Python
* LangGraph
* LangChain
* Google Gemini API
* dotenv
* Git & GitHub

## Project Structure

```text
LangGraph-AI-Agent/
│
├── data/
│   └── knowledge.txt
│
├── src/
│   ├── agent.py
│   ├── graph.py
│   ├── memory.py
│   ├── rag.py
│   └── tools.py
│
├── app.py
├── test.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### Clone Repository

```bash
git clone https://github.com/mradul9630/langgraph-ai-agent.git
cd langgraph-ai-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

## Run the Project

```bash
python app.py
```

## Example

```text
You: What is LangGraph?

Agent: LangGraph is a framework for building stateful, multi-step AI applications and agents.
```

## Future Enhancements

* Retrieval-Augmented Generation (RAG)
* Tool Calling
* Web Search Integration
* Multi-Agent Workflows
* Streamlit Chat Interface
* ChromaDB Vector Database
* Hugging Face Embeddings

## Author

**Mradul Upadhyay**

* GitHub: https://github.com/mradul9630
* LinkedIn: https://linkedin.com/in/mradul-upadhyay-90146329a/
