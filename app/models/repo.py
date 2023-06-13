from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()

class Repository(Base):
    __tablename__ = 'repository'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)
    owner = relationship("User", backref="repositories", cascade="all, delete, delete-orphan")
    desription = Column(String, nullable=False)
    stars = Column(String, nullable=False)
    forks = Column(Integer, nullable=False)
    createdAt = Column(String, nullable=False)
    updatedAt = Column(String, nullable=False)

def __repr__(self):
    return "<Repository(id= '%i', name= '%s', owner= '%s', description= '%s', stars= '%i', forks= '%i', createdAt= '%s')>"%(
        self.id, self.name, self.owner, self.description, self.stars, self.forks, self.createdAt, self.updatedAt
    )