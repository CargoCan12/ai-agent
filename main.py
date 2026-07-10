import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
#from vars import messages, model, args
#from client import client



parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

model = 'openrouter/free'

messages = [
    {
        "role": "user", "content": args.user_prompt
    }
]

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError("API Key didn't load")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


def main():
    print("Hello from ai!")
    response = client.chat.completions.create(model="openrouter/free", messages=messages,)
    if not response.usage:
        raise RuntimeError("API response appears to be malformed")
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
