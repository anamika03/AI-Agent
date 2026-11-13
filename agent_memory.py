import os, json
from openai import OpenAI
from tool_app import tools, execute_tool
from dotenv import load_dotenv
load_dotenv()

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

# TODO: Write the system prompt
SYSTEM_PROMPT = "You are a helpful personal assistant. Use your tools when you need real data."

questions = [
    "What's on my calander today?",
    "tell me about the standup.",
    "What time is my dentist?",
    "Am I free at 6pm?",
    "Summarise my day."
]

for que in questions:
    messages.append({"role": "user", "content": que})
    print(f"Messages in history: {len(messages)}")
    while True:
            response = client.chat.completions.create(
                model = "gpt-4.1-mini",
                messages=messages
            )
            if response.choices[0].finish_reason == "stop":
                reply = response.choices[0].message.content
                print(f"Q: {que}")
                print(f"A: {reply}\n")
                messages.append({"role": "assistant",
                                 "content": reply})
                break

def trim_history(messages, max_messages=6):
    if len(messages) > max_messages:
        return [messages[0]] + messages[-(max_messages - 1):]
    return messages

messages = trim_history(messages, max_messages=6)

while True:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages
    )
    finish_reason = response.choices[0].finish_reason
    if finish_reason == "stop":
        print(response.choices[0].message.content)
        break
    else:
        break
 