
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "openai/gpt-oss-120b"

def ask_ai(system_prompt, user_prompt, temperature=0.3, model=MODEL):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=temperature,
    )

    return response.choices[0].message.content


user_prompt = "Explain recursion with an example."

# Experiment 1: Change the system message
print("\n--- SYSTEM PROMPT COMPARISON ---")

prompts = [
    "You are a Python tutor. Explain simply.",
    "You are a strict interviewer. Be concise and technical.",
    "You are a storyteller. Use a real-world analogy."
]

for system_prompt in prompts:
    print(f"\nSystem: {system_prompt}")
    print(ask_ai(system_prompt, user_prompt, temperature=0.3))


# Experiment 2: Change the temperature
print("\n--- TEMPERATURE COMPARISON ---")

system_prompt = "You are a helpful AI assistant."
creative_prompt = "Suggest an unusual project using Python."

for temp in [0.0, 0.3, 0.7, 1.0]:
    print(f"\nTemperature: {temp}")
    print(ask_ai(system_prompt, creative_prompt, temperature=temp))


# Experiment 3: Change the model
print("\n--- MODEL COMPARISON ---")

models = [
    MODEL,
    # "another-supported-model-id"
]

for model in models:
    print(f"\nModel: {model}")
    print(ask_ai(system_prompt, user_prompt, temperature=0.3, model=model))
