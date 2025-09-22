from fastapi import APIRouter, Depends, HTTPException, status
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from database import getSession
from security.hashing import bcrypt_context, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM, oauth2_schema
from models import User
from datetime import timedelta, datetime, timezone
from jose import jwt, JWTError
from typing import Union
from fastapi.security import OAuth2PasswordRequestForm

auth_router = APIRouter(prefix='/auth', tags=['Authentication'])

@auth_router.post('/account_creation')
async def create_account(user_schema: UserBase, session: Session = Depends(getSession)):
    user = session.query(User).filter(User.username==user_schema.username).first()
    if user:
        raise HTTPException(status_code=400, detail="This user already exists")
    else:
        password_hash = bcrypt_context.hash(user_schema.password)
        new_user = User(username=user_schema.username, hashed_password=password_hash)
        session.add(new_user)
        session.commit()
        return {'message': f'User created! Username: {new_user.username}'}
    
def authenticate_user(username, password, session):
    user = session.query(User).filter(User.username==username).first()
    if not user or not bcrypt_context.verify(password, user.hashed_password):
        return False
    else:
        return user

def create_access_token(user_id, duration=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    expiration = datetime.now(timezone.utc) + duration
    dic_info = {'sub': str(user_id), 'exp': expiration}
    jwt_cod = jwt.encode(dic_info, SECRET_KEY, ALGORITHM)
    return jwt_cod

@auth_router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(getSession)):
    user = authenticate_user(form_data.username, form_data.password, session)
    if not user:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="User not found or invalid credentials", headers={'WWW-Authenticate': 'Bearer'})
    else:
        access_token = create_access_token(user.id)
        refresh_token = create_access_token(user.id, duration=timedelta(days=7))
        return {
            'access_token': access_token,
            'refresh_token': refresh_token,
            'token_type': 'Bearer'
        }
    
async def get_current_user(token: str = Depends(oauth2_schema), session: Session = Depends(getSession)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get('sub')
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = session.query(User).filter(User.id==user_id).first()
    if user is None:
        return credentials_exception
    return user

@auth_router.get('/me', response_model=UserDisplay)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user