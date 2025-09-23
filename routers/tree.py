from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import Link, User
from database import getSession
from routers.auth import get_current_user
from schemas import TreeBase

tree_router = APIRouter(prefix='/tree', tags=['Linktree'])

@tree_router.post('/create-link', status_code=status.HTTP_201_CREATED)
async def create_link(tree_base: TreeBase, session: Session = Depends(getSession), current_user: User = Depends(get_current_user)):
    link = session.query(Link).filter(Link.url == tree_base.url, Link.user_id == current_user.id).first()
    if link:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="This link already exists")

    new_link = Link(title=tree_base.title, url=tree_base.url, user_id=current_user.id)
    session.add(new_link)
    session.commit()
    session.refresh(new_link)
    return new_link

@tree_router.get('/my-links')
async def list_links(session: Session = Depends(getSession), current_user: User = Depends(get_current_user)):
    links = session.query(Link).filter(Link.user_id == current_user.id).all()
    return {
        'Username': current_user.username,
        'Linktree': links
    }

@tree_router.put('/links/{link_id}', status_code=status.HTTP_200_OK)
async def update_link(link_id: int, tree_base: TreeBase, session: Session = Depends(getSession), current_user: User = Depends(get_current_user)):
    link_to_update = session.query(Link).filter(Link.id == link_id, Link.user_id == current_user.id).first()

    if not link_to_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found")

    link_to_update.title = tree_base.title
    link_to_update.url = tree_base.url
    session.commit()
    session.refresh(link_to_update)
    return link_to_update

@tree_router.delete('/links/{link_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_link(link_id: int, session: Session = Depends(getSession), current_user: User = Depends(get_current_user)):
    link_to_delete = session.query(Link).filter(Link.id == link_id, Link.user_id == current_user.id).first()

    if not link_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found")

    session.delete(link_to_delete)
    session.commit()
    return