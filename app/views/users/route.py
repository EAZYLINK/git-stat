from flask import Blueprint, request
import sys, os, json
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_above = os.path.dirname(current_dir)
sys.path.append(folder_above)
from users.services import create_account, user_exist, get_user_by_username, update_user, delete_user
from utilities.user import hash_password, check_password

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.post('/signup')
def signup():
    data = request.values
    try:
        if user_exist(data['email'], data['username']) == True:
            return json.dumps({
                "status": 400,
                "message": "Username or email already exists"
            })
        elif user_exist(data['email'], data['username']) == False: 
            # try:
            new_user = create_account(data['email'], data['username'],  hash_password(data['password']))
            data = json.dumps({'email': new_user.email, 'username': new_user.username, 'password_hash': new_user.password_hash})
            return json.dumps({
            "status": 200,
            "message": "account created successfully",
            "data": "data",
                })
    except:
        return json.dumps({
            "status": 500,
            "message": "Server error",
            "data": "",
            })

@user_blueprint.post('/get_user/username')
def get_user():
    data = request.values
    try:
        user = get_user_by_username(data['username'])
        if user == None:
            return json.dumps({
                "status": 400,
                "message": "User not found",
                "data": "",
            })
        else:
            return json.dumps({
                "status": 200,
                "message": "User found",
                "data": json.dumps({'email': user.email, 'username': user.username, 'password_hash': user.password_hash}),
            })
    except:
        return json.dumps({
            "status": 500,
            "message": "Server error",
            "data": "",
        })

@user_blueprint.post('/update_user')
def update_user():
    data = request.values
    try:
        user_exist = user_exist(data['username'], data['password'])
        if user_exist == True:
            update_user(data['email'], data['username'], hash_password(data['password']))
            return json.dumps({
                "status": 200,
                "message": "User updated successfully",
                "data": "",
            })
    except:
        return json.dumps({
            "status": 500,
            "message": "Server error",
            "data": "",
        })