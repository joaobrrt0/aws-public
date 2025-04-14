# User Management API

Este repositório contém a implementação de uma API RESTful para gerenciamento de usuários usando AWS Lambda, API Gateway e DynamoDB. O objetivo é criar uma API serverless que permita criar, consultar, atualizar e excluir usuários de um banco de dados DynamoDB.

## Arquitetura

- **AWS Lambda**: Função serverless que processa as requisições.
- **API Gateway**: Exposição da API RESTful para interação com o cliente.
- **DynamoDB**: Banco de dados NoSQL utilizado para armazenar as informações dos usuários.

## Funcionalidades da API

- **POST /users**: Cria um novo usuário.
  - Exemplo de corpo da requisição:
    ```json
    {
      "user_id": "1",
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```
  
- **GET /users/{id}**: Recupera as informações de um usuário.
  - Exemplo de resposta:
    ```json
    {
      "user_id": "1",
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

- **PUT /users/{id}**: Atualiza as informações de um usuário.
  - Exemplo de corpo da requisição:
    ```json
    {
      "name": "Johnathan Doe",
      "email": "johnathan.doe@example.com"
    }
    ```

- **DELETE /users/{id}**: Deleta um usuário.

## Como Rodar

1. **Crie a tabela DynamoDB**:
   - Crie uma tabela chamada `Users` no DynamoDB com a chave primária `user_id`.

2. **Configuração do AWS Lambda e API Gateway**:
   - Crie uma função Lambda no AWS Console e faça upload do arquivo `lambda_function.py`.
   - Configure o API Gateway para chamar a função Lambda.

3. **Testando a API**:
   - Utilize ferramentas como [Postman](https://www.postman.com/) ou cURL para testar os endpoints da API.

## Exemplos de cURL

- **POST (criar usuário)**:
  ```bash
  curl -X POST https://your-api-id.execute-api.region.amazonaws.com/users \
  -H "Content-Type: application/json" \
  -d '{"user_id": "1", "name": "John Doe", "email": "john@example.com"}'
