from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Link, User
from routers.auth import getSession, get_current_user
from schemas import TreeBase

tree_router = APIRouter(prefix='/tree', tags=['Linktree'])

@tree_router.post('/create-link')
async def create_link(tree_base: TreeBase, session: Session = Depends(getSession), current_user: User = Depends(get_current_user)):
    link = session.query(Link).filter(Link.url==tree_base.url, Link.user_id==current_user.id).first()
    if link:
        raise HTTPException(status_code=400, detail="This link already exists")
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

@tree_router.delete('/delete-link/{link_id}')
async def delete_link(link_id: int, session: Session = Depends(getSession), current_user: User = Depends(get_current_user)):
    link = session.query(Link).filter(link_id==Link.id).first()
    if not link:
        return HTTPException(status_code=401, detail="Link not found")
    if link.user_id != current_user.id:
        return HTTPException(status_code=401, detail="This link is from another user")
    else:
        session.delete(link)
        session.commit()
        return {
            'Message': f'Link "{link.title}" was deleted'
        }