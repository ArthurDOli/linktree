from sqlalchemy import create_engine, Column, String, ForeignKey, Integer
from sqlalchemy.orm import declarative_base

db = create_engine('sqlite:///banco.db', connect_args={"check_same_thread": False})

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String)
    email = Column('email', String)
    password = Column('password', String)
    # links = Column('links', ) 
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
