from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

user_prompt = input("Enter your prompt: ")

response = client.responses.create(
    model="gpt-5.6-luna",
    input=user_prompt
)

print("\nAI Response:")
print(response.output_text)
