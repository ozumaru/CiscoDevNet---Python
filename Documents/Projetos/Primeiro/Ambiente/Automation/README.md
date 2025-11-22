```mermaid
flowchart TD
    A[Início] --> B[Receber lista de hosts]
    B --> C[Executar access_collect]
    C --> D[Converter saída em lista]
    D --> E[Extrair hostname]
    E --> F[Fim]
```