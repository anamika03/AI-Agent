# pip install openai
# pip install --upgrade pip

# TASK:Experiment with Temperature parameter in OpenAI API

from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY"
    )


response = client.chat.completions.create(
    model="gemini-1.5-flash",
    temperature=0.0,
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Be concise."},
        {"role": "user", "content": "Write a one-sentence story about a robot?"}
    ]
)

print(response.choices[0].message.content)