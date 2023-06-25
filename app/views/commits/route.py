import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_above = os.path.dirname(current_dir)
sys.path.append(folder_above)
from models.commit import Commit
from config import connect_db
from sqlalchemy import or_, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Session = connect_db
session = Session()

def create_commit(id, repositoryId, author, title, status, createdAt, updatedAt):
   new_commit = Commit(id, repositoryId, author, title, status, createdAt, updatedAt)
   session.add(new_commit)
   session.commit()
   session.flush()
   return new_commit

def get_commit_by_id(id):
    commit = session.query(Commit).filter(Commit.id == id).first()
    return commit

def get_commit_by_repositoryId(repositoryId):
    commit = session.query(Commit).filter(Commit.repositoryId == repositoryId).first()
    return commit

def get_commit_by_author(author):
    commit = session.query(Commit).filter(Commit.author == author).first()
    return commit

def get_commit_by_title(title):
    commit = session.query(Commit).filter(Commit.title == title).first()
    return commit

def get_commit_by_status(status):
    commit = session.query(Commit).filter(Commit.status == status).first()
    return commit

def get_commit_by_createdAt(createdAt):
    commit = session.query(Commit).filter(Commit.createdAt == createdAt).first()
    return commit

def get_commit_by_updatedAt(updatedAt):
    commit = session.query(Commit).filter(Commit.updatedAt == updatedAt).first()
    return commit

def get_all_commits():
    commits = session.query(Commit).all()
    return commits

def update_commit(id, repositoryId, author, title, status, createdAt, updatedAt):
    commit = session.query(Commit).filter(Commit.id == id).first()
    commit.repositoryId = repositoryId
    commit.author = author
    commit.title = title
    commit.status = status
    commit.createdAt = createdAt
    commit.updatedAt = updatedAt
    session.commit()
    return commit

def delete_commit(id):
    commit = session.query(Commit).filter(Commit.id == id).first()
    session.delete(commit)
    session.commit()
    return commit

def delete_all_commits():
    commits = session.query(Commit).all()
    for commit in commits:
        session.delete(commit)
        session.commit()
    return commits

engine = create_engine("sqlite:///git-stat.db")
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

def main():
    print("Commit Service")

if __name__ == "__main__":
    main()