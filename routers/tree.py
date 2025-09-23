from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Link, User
from routers.auth import get_current_user
from schemas import TreeBase
from database import getSession

tree_router = APIRouter(prefix='/tree', tags=['Linktree'])

@tree_router.post('/create-link')
async def create_link(tree_base: TreeBase, session: Session = Depends(getSession), current_user: User = Depends(get_current_user)):
    link = session.query(Link).filter(Link.url==tree_base.url, Link.user_id==current_user.id).first()
    if link:
        raise HTTPException(status_code=409, detail="This link already exists")
    else:
        new_link = Link(title=tree_base.title, url=tree_base.url, user_id=current_user.id)
        session.add(new_link)
        session.commit()
        return {'message': f'Link created! Title: {new_link.title}'}
    
@tree_router.get('/list-links')
async def list_links(session: Session = Depends(getSession), current_user: User = Depends(get_current_user)):
    links = session.query(Link).filter(current_user.id==Link.user_id).all()
    return {
        'Username': current_user.username,
        'Linktree': links
    }

@tree_router.delete('/delete-link/{link_title}')
async def delete_link(link_title: str, session: Session = Depends(getSession), current_user: User = Depends(get_current_user)):
    link = session.query(Link).filter(link_title==Link.title, current_user.id==Link.user_id).first()
    if not link:
        return HTTPException(status_code=404, detail="Link not found")
    else:
        session.delete(link)
        session.commit()
        return {
            'Message': f'Link "{link.title}" was deleted'
        }
    
@tree_router.put('/update-link/{link_title}')
async def update_link(link_title: str, tree_base: TreeBase, session: Session = Depends(getSession), current_user: User = Depends(get_current_user)):
    link = session.query(Link).filter(link_title==Link.title, current_user.id==Link.user_id).first()
    if not link:
        return HTTPException(status_code=404, detail="Link not found")
    link.title = tree_base.title
    link.url = tree_base.url
    session.commit()
    return {
        'Message': f'Link was updated! Updated title: "{link.title}"'
    }