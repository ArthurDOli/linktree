# uvicorn main:app --reload

from fastapi import FastAPI

app = FastAPI(title="Linktree")

from routers.auth import auth_router
from routers.tree import tree_router

app.include_router(auth_router)
app.include_router(tree_router)