import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE_URL", "https://api.openai.com/v1")
)


messages = [
    {"role": "system", "content": "You are a helpful assistant. Be concise."}
]

messages.append({
    "role": "user",
    "content": "What are three things an AI agent can do that a regular chatbot cannot?"
})

while True:
    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",
        messages=messages
    )
    if response.choices[0].finish_reason == "stop":
        print(response.choices[0].message.content)
        break
