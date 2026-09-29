from src.llm_client import ask_llm


def test_llm_returns_response():
    response = ask_llm("O que é teste de software?")

    assert response is not None
    assert response.strip() != ""


def test_llm_understands_software_testing():
    response = ask_llm(
        "Explique em uma frase o que é teste de software."
    )

    response_lower = response.lower()

    assert (
        "teste" in response_lower
        or "software" in response_lower
    )