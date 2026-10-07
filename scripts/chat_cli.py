from src.llm_client import LLMClient


def main():

    client = LLMClient()

    print("=== QA + IA Chat ===")
    print("Digite 'sair' para encerrar.")

    while True:

        prompt = input("\nVocê: ")

        if prompt.lower() == "sair":
            break

        try:

            response = client.chat(prompt)

            answer = response.choices[0].message.content

            print("\nLLM:")
            print(answer)

            print("\nTokens:")
            print(response.usage)

        except Exception as exc:

            print(f"\nErro: {type(exc).__name__}")
            print(exc)


if __name__ == "__main__":
    main()