from fastapi import APIRouter

auth_router = APIRouter(prefix='/auth', tags=['Authentication'])

@auth_router.post('/account_creation')
async def create_account():
    return {'mensagem': 'Hello World'}