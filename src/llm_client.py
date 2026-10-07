import os
import time

from dotenv import load_dotenv
from groq import (
    Groq,
    RateLimitError,
    APIStatusError,
    APIConnectionError,
    APITimeoutError,
)

load_dotenv()


class LLMClient:

    def __init__(
        self,
        model: str = "openai/gpt-oss-20b",
        timeout: float = 10.0,
    ):
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            raise ValueError("GROQ_API_KEY não configurada.")

        self.model = model

        # max_retries=0 é intencional nesta etapa.
        # Queremos controlar e testar nosso próprio retry.
        self.client = Groq(
            api_key=api_key,
            timeout=timeout,
            max_retries=0,
        )

    def chat(
        self,
        prompt: str,
        temperature: float = 0.2,
        max_tokens: int = 300,
    ):

        if prompt is None:
            raise ValueError("Prompt não pode ser None.")

        if not isinstance(prompt, str):
            raise TypeError("Prompt deve ser uma string.")

        messages = [
            {
                "role": "user",
                "content": prompt,
            }
        ]

        return self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    def chat_with_retry(
        self,
        prompt: str,
        max_attempts: int = 3,
        temperature: float = 0.2,
        max_tokens: int = 300,
    ):

        last_exception = None

        for attempt in range(max_attempts):

            try:
                return self.chat(
                    prompt=prompt,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )

            except RateLimitError as exc:

                last_exception = exc

                wait_time = min(
                    2 ** attempt,
                    30,
                )

                time.sleep(wait_time)

            except (APITimeoutError, APIConnectionError) as exc:

                last_exception = exc

                wait_time = min(
                    2 ** attempt,
                    30,
                )

                time.sleep(wait_time)

            except APIStatusError as exc:

                # Erros 5xx podem ser transitórios.
                if exc.status_code >= 500:

                    last_exception = exc

                    wait_time = min(
                        2 ** attempt,
                        30,
                    )

                    time.sleep(wait_time)

                else:
                    raise

        raise last_exception