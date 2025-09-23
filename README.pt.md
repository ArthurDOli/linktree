# Linktree API com FastAPI

O Linktree API é um projeto backend desenvolvido em Python com FastAPI que replica a funcionalidade principal do Linktree. A aplicação permite que utilizadores se registem, autentiquem e gerenciem uma lista de links pessoais, tudo através de uma API RESTful.

## Funcionalidades

- **Autenticação Segura de Utilizador:** Sistema completo de criação de conta e login utilizando tokens JWT para segurança.
- **Hashing de Senhas:** As senhas dos utilizadores são armazenadas de forma segura utilizando o algoritmo bcrypt.
- **Gestão de Links (CRUD):**
  - **Criar:** Endpoint protegido para utilizadores autenticados adicionarem novos links ao seu perfil.
  - **Ler:** Endpoint para visualizar a lista de links de um utilizador.
  - **Atualizar:** Endpoint para editar um link existente, com verificação de propriedade antes de aplicar as alterações.
  - **Apagar:** Endpoint protegido para remover um link específico, com verificação para garantir que apenas o dono do link o possa apagar.

## Tecnologias Utilizadas

- **Backend:** Python, FastAPI
- **Base de Dados:** SQLite com SQLAlchemy

## Instalação e Configuração

Siga os passos abaixo para configurar e executar o projeto localmente:

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/ArthurDOli/linktree.git
    cd linktree
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    # No Windows
    venv\Scripts\activate
    # No macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    (Nota: Crie um arquivo `requirements.txt` primeiro executando `pip freeze > requirements.txt` no seu terminal)

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    Crie um ficheiro `.env` na raiz do projeto e adicione as seguintes variáveis. Estes valores são essenciais para a segurança dos tokens JWT.

    ```
    SECRET_KEY='sua_secret_key'
    ALGORITHM='HS26'
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

5.  **Execute a aplicação:**
    O projeto está configurado para usar o Uvicorn, um servidor ASGI de alta performance.
    ```bash
    uvicorn main:app --reload
    ```
    - A API estará disponível em `http://127.0.0.1:8000`.
    - A documentação interativa estará em `http://127.0.0.1:8000/docs`.

## Estrutura do Projeto

```bash
linktree/
├── routers/
│   ├── auth.py
│   └── tree.py
├── security/
│   └── hashing.py
├── .env
├── .gitignore
├── database.py
├── main.py
├── models.py
└── schemas.py
```
