from fastapi import APIRouter, Depends, HTTPException, status
from schemas import UserBase
from sqlalchemy.orm import Session
from database import getSession
from security.hashing import bcrypt_context
from models import User

auth_router = APIRouter(prefix='/auth', tags=['Authentication'])

@auth_router.post('/account_creation')
async def create_account(user_schema: UserBase, session: Session = Depends(getSession)):
    usuario = session.query(User).filter(User.username==user_schema.username).first()
    if usuario:
        raise HTTPException(status_code=400, detail="This user already exists!")
    else:
        password_hash = bcrypt_context.hash(user_schema.password)
        new_user = User(username=user_schema.username, hashed_password=password_hash)
        session.add(new_user)
        session.commit()
        return {'message': f'User created! Username: {new_user.username}'}