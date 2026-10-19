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

    
    messages = [
        {
            "role": "system",
            "content": """
            You are a friendly Python programming tutor.

            Follow these rules:
            1. Explain concepts in simple language.
            2. Give short, clear explanations.
            3. Provide Python code examples when useful.
            4. Explain code step by step.
            5. Help users debug errors.
            6. Encourage the user to solve problems independently.
            """
        }
    ]

    print("Python AI Tutor is ready!")
    print("Ask questions or type 'exit' to quit.\n")

    while True:
        prompt = input("You: ").strip()

        if prompt.lower() == "exit":
            print("AI Tutor: Happy learning! Goodbye.")
            break

        if not prompt:
            continue

        # 3. Conversation history
        messages.append({
            "role": "user",
            "content": prompt
        })

        try:
            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )

            answer = response.choices[0].message.content

            print(f"\nAI Tutor: {answer}\n")

            # Save the AI response for future context
            messages.append({
                "role": "assistant",
                "content": answer
            })

        except APIError as error:
            print(f"API Error: {error}")

            # Remove the failed user message so it isn't
            # accidentally retained as conversation history.
            messages.pop()

        except Exception as error:
            print(f"Unexpected error: {error}")
            messages.pop()


if __name__ == "__main__":
    main()