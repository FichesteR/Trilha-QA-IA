import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role": "user", "content": "Olá"}],
    temperature=0.2,
)

print("Resposta:", response.choices[0].message.content)
print("Uso:", response.usage)  # Imprime prompt_tokens, completion_tokens, total_tokens