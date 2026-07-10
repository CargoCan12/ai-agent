import argparse
model = 'openrouter/free'
messages=[
    {
        "role": "user",
        "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    }
]

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()
# Now we can access `args.user_prompt`