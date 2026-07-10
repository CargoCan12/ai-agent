import argparse


parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()
# Now we can access `args.user_prompt`

model = 'openrouter/free'

messages = [
    {
        "role": "user", "content": args.user_prompt
    }
]