from vars import messages, model
from client import client


def main():
    print("Hello from ai!")
    response = client.chat.completions.create(model = model, messages=messages)
    if response.usage != None:
        print(f"User prompt: {messages[0]['content']}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
        print(response.choices[0].message.content)
    else:
        raise RuntimeError("Did not complete as dialed")

if __name__ == "__main__":
    main()
