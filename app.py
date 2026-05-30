from src.graph import app

while True:

    query = input("\nYou: ")

    if query.lower() == "exit":
        break

    result = app.invoke(
        {
            "user_input": query
        }
    )

    print(
        "\nAgent:",
        result["response"]
    )