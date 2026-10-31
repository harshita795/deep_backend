import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI


def main():
    parser = argparse.ArgumentParser(description="AI Agent")
    parser.add_argument(
        "prompt",
        type=str,
        help="The prompt to send to the AI",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )
    args = parser.parse_args()
    user_prompt = args.prompt

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key is None:
        raise RuntimeError(
            "OPENROUTER_API_KEY is missing. "
            "Please add it to your .env file."
        )

    # Create a client configured to use OpenRouter
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    # Store the conversation as a list of messages
    messages = [
        {"role": "user", "content": user_prompt,},
    ]

    # Send the conversation to the AI model
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
    )

    if response.usage is None:
        raise RuntimeError("Token usage information is missing.")

    if args.verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    # Print the AI's answer
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
