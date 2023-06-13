import sys, os
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_above = os.path.dirname(current_dir)
sys.path.append(folder_above)
from models.repo import Repository
from config.db import connect_db
from sqlalchemy import or_, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Session = connect_db
session = Session()

def create_repository(id, userId, name, description, status, createdAt, updatedAt):
    new_repository = Repository(id, userId, name, description, status, createdAt, updatedAt)
    session.add(new_repository)
    session.commit()
    session.flush()
    return new_repository

def get_repository_by_id(id):
    repository = session.query(Repository).filter(Repository.id == id).first()
    return repository

def get_repository_by_userId(userId):
    repository = session.query(Repository).filter(Repository.userId == userId).first()
    return repository

def get_repository_by_name(name):
    repository = session.query(Repository).filter(Repository.name == name).first()
    return repository

def get_repository_by_description(description):
    repository = session.query(Repository).filter(Repository.description == description).first()
    return repository

def get_repository_by_status(status):
    repository = session.query(Repository).filter(Repository.status == status).first()
    return repository

def get_repository_by_createdAt(createdAt):
    repository = session.query(Repository).filter(Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_updatedAt(updatedAt):
    repository = session.query(Repository).filter(Repository.updatedAt == updatedAt).first()
    return repository

def get_all_repositories():
    repositories = session.query(Repository).all()
    return repositories

def update_repository(id, userId, name, description, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.id == id).first()
    repository.userId = userId
    repository.name = name
    repository.description = description
    repository.status = status
    repository.createdAt = createdAt
    repository.updatedAt = updatedAt
    session.commit()
    session.flush()
    return repository  

def delete_repository(id):
    repository = session.query(Repository).filter(Repository.id == id).first()
    session.delete(repository)
    session.commit()
    session.flush()
    return repository 

def delete_all_repositories():
    repositories = session.query(Repository).all()
    for repository in repositories:
        session.delete(repository)
        session.commit()
        session.flush()
    return repositories

def get_repository_by_userId_and_name(userId, name):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name).first()
    return repository

def get_repository_by_userId_and_id(userId, id):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.id == id).first()
    return repository

def get_repository_by_userId_and_name_and_id(userId, name, id):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_description(userId, name, id, description):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.description == description).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_description_and_status(userId, name, id, description, status):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.description == description, Repository.status == status).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_description_and_status_and_createdAt(userId, name, id, description, status, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_description_and_status_and_createdAt_and_updatedAt(userId, name, id, description, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_description_and_status_and_updatedAt(userId, name, id, description, status, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.description == description, Repository.status == status, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_description_and_createdAt(userId, name, id, description, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.description == description, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_status_and_createdAt(userId, name, id, status, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.status == status, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_status_and_updatedAt(userId, name, id, status, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.status == status, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_createdAt_and_updatedAt(userId, name, id, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_description_and_status_and_createdAt(userId, name, description, status, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_name_and_description_and_status_and_updatedAt(userId, name, description, status, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.description == description, Repository.status == status, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_description_and_createdAt_and_updatedAt(userId, name, description, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.description == description, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_status_and_createdAt_and_updatedAt(userId, name, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_id_and_description_and_status_and_createdAt(userId, id, description, status, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.id == id, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_id_and_description_and_status_and_updatedAt(userId, id, description, status, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.id == id, Repository.description == description, Repository.status == status, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_id_and_description_and_createdAt_and_updatedAt(userId, id, description, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.id == id, Repository.description == description, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_id_and_status_and_createdAt_and_updatedAt(userId, id, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.id == id, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_description_and_status_and_createdAt_and_updatedAt(userId, description, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_name_and_id_and_description_and_status_and_createdAt(name, id, description, status, createdAt):
    repository = session.query(Repository).filter(Repository.name == name, Repository.id == id, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_name_and_id_and_description_and_status_and_updatedAt(name, id, description, status, updatedAt):
    repository = session.query(Repository).filter(Repository.name == name, Repository.id == id, Repository.description == description, Repository.status == status, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_name_and_id_and_description_and_createdAt_and_updatedAt(name, id, description, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.name == name, Repository.id == id, Repository.description == description, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_name_and_id_and_status_and_createdAt_and_updatedAt(name, id, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.name == name, Repository.id == id, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_name_and_description_and_status_and_createdAt_and_updatedAt(name, description, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.name == name, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_id_and_description_and_status_and_createdAt_and_updatedAt(id, description, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.id == id, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_description_and_status(userId, name, id, description, status):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.description == description, Repository.status == status).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_description_and_createdAt(userId, name, id, description, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.description == description, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_description_and_updatedAt(userId, name, id, description, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.description == description, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_status_and_createdAt(userId, name, id, status, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.status == status, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_status_and_updatedAt(userId, name, id, status, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.status == status, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_createdAt_and_updatedAt(userId, name, id, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_description_and_status_and_createdAt(userId, name, description, status, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_name_and_description_and_status_and_updatedAt(userId, name, description, status, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.description == description, Repository.status == status, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_description_and_createdAt_and_updatedAt(userId, name, description, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.description == description, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_status_and_createdAt_and_updatedAt(userId, name, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_id_and_description_and_status_and_createdAt(userId, id, description, status, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.id == id, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_id_and_description_and_status_and_updatedAt(userId, id, description, status, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.id == id, Repository.description == description, Repository.status == status, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_id_and_description_and_createdAt_and_updatedAt(userId, id, description, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.id == id, Repository.description == description, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_id_and_status_and_createdAt_and_updatedAt(userId, id, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.id == id, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_description_and_status_and_createdAt_and_updatedAt(userId, description, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_name_and_id_and_description_and_status_and_createdAt(name, id, description, status, createdAt):
    repository = session.query(Repository).filter(Repository.name == name, Repository.id == id, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_name_and_id_and_description_and_status_and_updatedAt(name, id, description, status, updatedAt):
    repository = session.query(Repository).filter(Repository.name == name, Repository.id == id, Repository.description == description, Repository.status == status, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_name_and_id_and_description_and_createdAt_and_updatedAt(name, id, description, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.name == name, Repository.id == id, Repository.description == description, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_name_and_id_and_status_and_createdAt_and_updatedAt(name, id, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.name == name, Repository.id == id, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_name_and_description_and_status_and_createdAt_and_updatedAt(name, description, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.name == name, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_id_and_description_and_status_and_createdAt_and_updatedAt(id, description, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.id == id, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_description_and_status(userId, name, id, description, status):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.description == description, Repository.status == status).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_description_and_createdAt(userId, name, id, description, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.description == description, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_description_and_updatedAt(userId, name, id, description, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.description == description, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_status_and_createdAt(userId, name, id, status, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.status == status, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_status_and_updatedAt(userId, name, id, status, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.status == status, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_createdAt_and_updatedAt(userId, name, id, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_description_and_status_and_createdAt(userId, name, description, status, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_name_and_description_and_status_and_updatedAt(userId, name, description, status, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.description == description, Repository.status == status, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_description_and_createdAt_and_updatedAt(userId, name, description, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.description == description, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_status_and_createdAt_and_updatedAt(userId, name, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_id_and_description_and_status_and_createdAt(userId, id, description, status, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.id == id, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_id_and_description_and_status_and_updatedAt(userId, id, description, status, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.id == id, Repository.description == description, Repository.status == status, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_id_and_description_and_createdAt_and_updatedAt(userId, id, description, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.id == id, Repository.description == description, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_id_and_status_and_createdAt_and_updatedAt(userId, id, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.id == id, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_description_and_status_and_createdAt_and_updatedAt(userId, description, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_name_and_id_and_description_and_status_and_createdAt(name, id, description, status, createdAt):
    repository = session.query(Repository).filter(Repository.name == name, Repository.id == id, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_name_and_id_and_description_and_status_and_updatedAt(name, id, description, status, updatedAt):
    repository = session.query(Repository).filter(Repository.name == name, Repository.id == id, Repository.description == description, Repository.status == status, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_name_and_id_and_description_and_createdAt_and_updatedAt(name, id, description, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.name == name, Repository.id == id, Repository.description == description, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_name_and_id_and_status_and_createdAt_and_updatedAt(name, id, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.name == name, Repository.id == id, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_name_and_description_and_status_and_createdAt_and_updatedAt(name, description, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.name == name, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_id_and_description_and_status_and_createdAt_and_updatedAt(id, description, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.id == id, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_description_and_status(userId, name, id, description, status):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.description == description, Repository.status == status).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_description_and_createdAt(userId, name, id, description, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.description == description, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_description_and_updatedAt(userId, name, id, description, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.description == description, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_status_and_createdAt(userId, name, id, status, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.status == status, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_status_and_updatedAt(userId, name, id, status, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.status == status, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_id_and_createdAt_and_updatedAt(userId, name, id, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.id == id, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_description_and_status_and_createdAt(userId, name, description, status, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_name_and_description_and_status_and_updatedAt(userId, name, description, status, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.description == description, Repository.status == status, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_description_and_createdAt_and_updatedAt(userId, name, description, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.description == description, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_name_and_status_and_createdAt_and_updatedAt(userId, name, status, createdAt, updatedAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.name == name, Repository.status == status, Repository.createdAt == createdAt, Repository.updatedAt == updatedAt).first()
    return repository

def get_repository_by_userId_and_id_and_description_and_status_and_createdAt(userId, id, description, status, createdAt):
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.id == id, Repository.description == description, Repository.status == status, Repository.createdAt == createdAt).first()
    return repository

def get_repository_by_userId_and_id_and_description_and_status_and_updatedAt(userId, id, description, status, updatedAt):   
    repository = session.query(Repository).filter(Repository.userId == userId, Repository.id == id, Repository.description == description, Repository.status == status, Repository.updatedAt == updatedAt).first()
    return repository

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

#end of file