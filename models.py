from sqlalchemy import create_engine, Column, String, ForeignKey, Integer
from sqlalchemy.orm import declarative_base, relationship

db = create_engine('sqlite:///banco.db', connect_args={"check_same_thread": False})

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, unique=True, index=True)
    hashed_password = Column('password', String)
    links = relationship('Link', cascade='all, delete')
    
class Link(Base):
    __tablename__ = 'links'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column('title', String)
    url = Column('url', String, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))

Base.metadata.create_all(bind=db)