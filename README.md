# Linktree API with FastAPI

The Linktree API is a backend project developed in Python with FastAPI that replicates the core functionality of Linktree. The application allows users to register, authenticate, and manage a list of personal links, all through a RESTful API.

## Features

- **Secure User Authentication:** A complete system for account creation and login using JWT tokens for security.
- **Password Hashing:** User passwords are securely stored using the bcrypt algorithm.
- **Link Management (CRUD):**
  - **Create:** A protected endpoint for authenticated users to add new links to their profile.
  - **Read:** An endpoint to view a user's list of links.
  - **Update:** A endpoint to edit an existing link, verifying ownership before applying changes.
  - **Delete:** A protected endpoint to remove a specific link, with verification to ensure only the link's owner can delete it.

## Technologies Used

- **Backend:** Python, FastAPI
- **Database:** SQLite with SQLAlchemy

## Installation and Setup

Follow the steps below to set up and run the project locally:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/ArthurDOli/linktree.git
    cd linktree
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    (Note: First, create a `requirements.txt` file by running `pip freeze > requirements.txt` in your terminal)

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure the environment variables:**
    Create a `.env` file in the root of the project and add the following variables. These values are essential for the security of the JWT tokens.

    ```
    SECRET_KEY='your_secret_key'
    ALGORITHM='HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    ```

5.  **Run the application:**
    The project is configured to use Uvicorn, a high-performance ASGI server.
    ```bash
    uvicorn main:app --reload
    ```
    - The API will be available at `http://127.0.0.1:8000`.
    - The interactive documentation will be at `http://127.0.0.1:8000/docs`.

## Project Structure

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
