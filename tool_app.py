
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv(
        "OPENAI_API_BASE_URL",
        "https://api.openai.com/v1"
    )
)

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
    return "10am: Standup, 2pm: Dentist"


def execute_tool(name, args):
    if name == "check_calendar":
        return check_calendar(**args)

    return f"Unknown tool: {name}"


def run_demo():
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant. Be concise."
        },
        {
            "role": "user",
            "content": "What's on my calendar today?"
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=messages,
        tools=tools
    )

    msg = response.choices[0].message

    if msg.tool_calls:
        messages.append(msg.model_dump(exclude_none=True))

        for tc in msg.tool_calls:
            result = execute_tool(
                tc.function.name,
                json.loads(tc.function.arguments)
            )

            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": result
            })

        final = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=messages,
            tools=tools
        )

        print(final.choices[0].message.content)

    else:
        print(msg.content)


# Run demo only when this file is executed directly
if __name__ == "__main__":
    run_demo()
