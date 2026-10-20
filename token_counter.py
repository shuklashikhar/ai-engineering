
import tiktoken

MODEL = "gpt-4o"

# Example prices per 1 million tokens (USD).
# Replace these with your chosen model's actual prices.
INPUT_PRICE = 0.50
OUTPUT_PRICE = 2.00

encoding = tiktoken.encoding_for_model(MODEL)


def count_tokens(text):
    return len(encoding.encode(text))


def calculate_cost(input_tokens, output_tokens):
    input_cost = input_tokens * INPUT_PRICE / 1_000_000
    output_cost = output_tokens * OUTPUT_PRICE / 1_000_000
    return input_cost + output_cost


requests = [
    {
        "prompt": "Explain Python loops.",
        "estimated_output_tokens": 200
    },
    {
        "prompt": "Explain RAG vs fine-tuning with examples.",
        "estimated_output_tokens": 500
    },
    {
        "prompt": "Write a Python chatbot using conversation history.",
        "estimated_output_tokens": 1000
    }
]

total_cost = 0

for request in requests:
    input_tokens = count_tokens(request["prompt"])
    output_tokens = request["estimated_output_tokens"]

    cost = calculate_cost(input_tokens, output_tokens)
    total_cost += cost

    print(f"\nPrompt: {request['prompt']}")
    print(f"Input tokens: {input_tokens}")
    print(f"Estimated output tokens: {output_tokens}")
    print(f"Estimated cost: ${cost:.8f}")

print(f"\nTotal estimated cost: ${total_cost:.8f}")
