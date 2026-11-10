import os
from flask import json
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE_URL", "https://api.openai.com/v1")
)

model = "openai/gpt-4.1-mini"
messages = [
    {"role": "system", 
     "content": "You are a helpful assistant. Be concise. Use your tools when you need real data."}
]

tools = [
    {
        "type": "function",
        "function": {
            "name": "check_calendar",
            "description": "Check calendar",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "The date to check"
                    }
                },
                "required": ["date"]
            }
        }
    }
]

def check_calendar(date):
    return "10am: Standup, 2pm:Dentist, 4pm: Meeting with team"

while True:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools
    )
    finish_reason = response.choices[0].finish_reason
    msg = response.choices[0].message
    messages.append(msg)

    if finish_reason == "stop":
        print(msg.content)
        break

    if finish_reason == "tool_calls":
        for tc in msg.tool_calls:
            name = tc.function.name
            args = json.loads(tc.function.arguments)
            result = check_calendar(**args)
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": result
            })
            