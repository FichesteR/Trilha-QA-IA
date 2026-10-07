| ID      | Cenário           | Entrada              | Esperado               |
| ------- | ----------------- | -------------------- | ---------------------- |
| API-001 | Request válido    | prompt válido        | 200                    |
| API-002 | Prompt vazio      | `""`                 | erro ou tratamento     |
| API-003 | Model vazio       | `""`                 | 400                    |
| API-004 | Model inexistente | fake-model           | erro                   |
| API-005 | API key inválida  | chave inválida       | 401                    |
| API-006 | Payload inválido  | JSON inválido        | 400                    |
| API-007 | max tokens baixo  | `1`                  | resposta limitada      |
| API-008 | Unicode           | acentos/emojis       | resposta válida        |
| API-009 | Prompt gigante    | string longa         | tratamento adequado    |
| API-010 | Timeout           | rede lenta           | retry/falha controlada |
| API-011 | Rate limit        | muitas requisições   | 429                    |
| API-012 | Streaming         | `stream=True`        | chunks                 |
| API-013 | System prompt     | system + user        | comportamento esperado |
| API-014 | Injection         | instrução maliciosa  | aplicação trata        |
| API-015 | Concorrência      | requests simultâneos | controle de limite     |
