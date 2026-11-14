import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_API_BASE_URL", "https://api.openai.com/v1")
)

model = "gpt-4.1-mini"
messages = [
    {"role": "system", 
     "content": "You are a helpful assistant. Be concise. Use your tools when you need real data."}
]