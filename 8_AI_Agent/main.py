import os
import argparse
import json

from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions

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
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt},
    ]

    # Send the conversation to the AI model
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
        temperature=0,
    )

    if response.usage is None:
        raise RuntimeError("Token usage information is missing.")

    if args.verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")

    # Extract the assistant's message.    
    message = response.choices[0].message
    
    # Check whether the LLM requested any tools.
    if message.tool_calls:
        for tool_call in message.tool_calls:
            function_args = json.loads(
                tool_call.function.arguments or "{}"
            )

            print(
                f"Calling function: "
                f"{tool_call.function.name}({function_args})"
            )
    else:
        print(message.content)



if __name__ == "__main__":
    main()
