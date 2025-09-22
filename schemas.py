from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    password: str
    class Config:
        from_attributes = True

class TreeBase(BaseModel):
    title: str
    url: str
    class Config:
        from_attributes = True

class UserDisplay(BaseModel):
    id: int
    username: str
    class Config:
        from_attributes = True