from flask import Flask, session, jsonify
import os
from dotenv import load_dotenv
from models.user import User
from utilities.user import check_password
from flask_jwt import jwt, jwt_required, current_identity
   

def user_exist(username, password):
    user = session.query(User).filter(User.username==username).first()
    if user == None:
        return False
    if check_password(user.password_hash, password):
        return {'status': True, 'user': user}
    return False  


def create_access_token(payload):
    access_token = jwt.jwt_encode_callback(user_exist['user'])
    return jsonify({'token': access_token.decode('UTF-8')})

def login_required():
    return jwt_required()