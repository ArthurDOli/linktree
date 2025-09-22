from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Link, User
from auth import getSession
from schemas import TreeBase

tree_router = APIRouter(prefix='tree', tags=['Linktree'])

@tree_router.post('/create-link')
async def create_link(tree_base: TreeBase, session: Session = Depends(getSession)):
    new_link = Link()