import os

from dotenv import load_dotenv
from groq import Groq, APIError

load_dotenv()

def main():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("Error: GROQ_API_KEY not found in environment variables.")
        return

    client = Groq(api_key=api_key)
    prompt = input("Enter your prompt: ").strip()

    if not prompt:
        print("Error: Prompt cannot be empty.")
        return

    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
             messages=[
                {
                    "role": "system",
                    "content": "You are a helpful AI assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=500
        )
        answer = response.choices[0].message.content
        print("\nAI Response:\n")
        print(answer)

    except APIError as e:
        print(f"API Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()