# Week 1 — Groq API Contract

## Endpoint

POST /openai/v1/chat/completions

## Required fields

### model

Tipo:
string

Obrigatório:
sim

Exemplo:
openai/gpt-oss-20b

### messages

Tipo:
array

Obrigatório:
sim

Formato:

[
  {
    "role": "user",
    "content": "..."
  }
]

## Roles

- system
- user
- assistant

## Optional parameters

- temperature
- max_tokens / max_completion_tokens
- top_p
- stop
- stream

## Success

HTTP 200

Expected:

- response id
- choices
- assistant message
- usage

## Error scenarios

400 Bad Request | payload inválido
401 Unauthorized | autenticação
403 Forbidden | permissão
404 Not Found | recurso/modelo
413 Request Entity Too Large | payload grande
422 Unprocessable Entity | erro de processamento, não passa nas regras
429 Too Many Requests | rate limit
500 Internal Server Error | erro servidor
502 Bad Gateway | servidor intermediário recebeu uma resposta inválida da origem
503 Service Unavailable | servidor está temporariamente indisponível

## Rate Limit Headers

- x-ratelimit-limit-requests
- x-ratelimit-remaining-requests
- x-ratelimit-reset-requests
- x-ratelimit-limit-tokens
- x-ratelimit-remaining-tokens
- x-ratelimit-reset-tokens
- retry-after