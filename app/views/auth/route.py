from flask import Blueprint, request, url_for, session, render_template, redirect
from flask_jwt import jwt_required
import sys, os, json
from dotenv import load_dotenv
from flask_oauthlib.client import OAuth
import requests
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_above = os.path.dirname(current_dir)
sys.path.append(folder_above)
from auth.service import  user_exist, create_access_token
from dashboard.route import dashboard_blueprint

load_dotenv('.env')

auth_blueprint = Blueprint('auth_blueprint', __name__)
oauth = OAuth(auth_blueprint)
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CLIENT_SECRET')


github = oauth.remote_app(
    'github',
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    request_token_params={'scope': 'user:email'},
    base_url='https://api.github.com/',
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize'
)

# This is the route that will be called when the user clicks the login button
@auth_blueprint.route('/login/github')
def login_with_github():
    return github.authorize(callback=url_for('auth_blueprint.authorized', _external=True))

@github.tokengetter
def get_github_oauth_token():
    return session.get('oauth_token')

# This is the callback route that github will redirect to after login
@auth_blueprint.route('/login/github/authorized')
def authorized():
    code = request.args.get('code')
    if code is None:
        return redirect(url_for('main_blueprint.login', message=request.args.get('error')))
    response = github.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Authorization failed!'
    session['oauth_token'] = (response['access_token'], '')
    user = github.get('user')
    return redirect(url_for('dashboard_blueprint.view_dashboard', username=user.data['login']))

# This is the route that will be called when the user clicks the login button
@auth_blueprint.route('/login/<message>')
def login(message):
    data = request.values
    try:
        user_exist = user_exist(data['username'], data['password'])
        if user_exist == True:
            token = create_access_token(payload=user_exist['user'])
            session['token'] = token
            return redirect(url_for('dashboard_blueprint.dashboard', username=user_exist['user'].username))
        elif user_exist == False:
            return redirect(url_for('auth_blueprint.login', message='Invalid username or password'))
    except:
        return render_template('login.html', message='An error occured')
    
@auth_blueprint.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return 'You dont have access to this page'
