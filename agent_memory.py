import os, json
from openai import OpenAI
from tool_app import tools, execute_tool
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE_URL", "https://api.openai.com/v1")
)

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
    answer = run_agent(messages)
    print(f"Messages in history: {len(messages)}")

 