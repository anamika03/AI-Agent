# pip install openai
# pip install --upgrade pip

# TASK:Experiment with Temperature parameter in OpenAI API
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


response = client.chat.completions.create(
    model="gpt-4.1-mini",
    temperature=0.7,
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Be concise."},
        {"role": "user", "content": "Write a one-sentence story about a robot?"}
    ]
)

print(response.choices[0].message.content)