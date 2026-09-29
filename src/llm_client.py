import os
from dotenv import load_dotenv
from groq import Groq

# Carrega as variáveis do arquivo .env
load_dotenv()

def ask_llm(texto_prompt: str) -> str:
    """Envia uma pergunta para a API da Groq e retorna a resposta de forma ultra rápida."""
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY não foi encontrada no arquivo .env")
        
    # Inicializa o cliente oficial da Groq
    client = Groq(api_key=api_key)
    
    # Modelo de produção ativo e super veloz da Groq
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": texto_prompt,
            }
        ],
        model="openai/gpt-oss-20b",
    )
        
    # Adicionado [0] para pegar o primeiro item da lista de escolhas
    return chat_completion.choices[0].message.content.strip()
