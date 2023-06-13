from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()

class Pullrequest(Base):
    __tablename__ = 'pullrequest'
    id = Column(Integer, nullable=False, primary_key=True)
    repositoryId = relationship("Pullrequest", backref="commits", cascade="all, delete, delete-orphan")
    author = relationship("User", backref="repositories", cascade="all, delete, delete-orphan")
    title = Column(String, nullable=False)
    status = Column(String, nullable=False)
    createdAt = Column(String, nullable=False)
    updatedAt = Column(String, nullable=False)

def __repr__(self):
    return "<Commit(id= '%i', repositoryId= '%s', author= '%s', title= '%s', status= '%s', createdAt= '%s')>"%(
        self.id, self.repositoryId, self.author, self.title, self.status, self.createdAt, self.updatedAt
    )