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

load_dotenv('.env')

auth_blueprint = Blueprint('auth_blueprint', __name__)
oauth = OAuth(auth_blueprint)
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CLIENT_SECRET')


# github = oauth.remote_app(
#     'github',
#     consumer_key=CONSUMER_KEY,
#     consumer_secret=CONSUMER_SECRET,
#     request_token_params={'scope': 'user:email'},
#     base_url='https://api.github.com/',
#     state='git-stat',
#     allow_signup=True,
#     request_token_url=None,
#     access_token_method='POST',
#     access_token_url='https://github.com/login/oauth/access_token',
#     authorize_url='https://github.com/login/oauth/authorize'
# )

# This is the route that will be called when the user clicks the login button
@auth_blueprint.route('/login/github')
def login_with_github():
    # return github.authorize(callback=url_for('auth_blueprint.authorized'))
    params = {
        'client_id': CONSUMER_KEY,
        'redirect_uri': 'http://127.0.0.1:8000/auth/login/github/authorized',
        'scope': 'user:email',
        'state': 'git-stat',
        'allow_signup': True
    }
    url = 'https://github.com/login/oauth/authorize'
    return redirect(url + '?' + 'client_id=' + params['client_id'] + '&' + 'redirect_uri=' + params['redirect_uri'] + '&' + 'scope=' + params['scope'] + '&' + 'state=' + params['state'] + '&' + 'allow_signup=' + str(params['allow_signup']))

# This is the callback route that github will redirect to after login
@auth_blueprint.route('/login/github/authorized')
def authorized():
    code = request.args.get('code')
    if code is None:
        return redirect(url_for('main_blueprint.login', message=request.args.get('error')))
    params = {
        'client_id': CONSUMER_KEY,
        'client_secret': CONSUMER_SECRET,
        'code': code,
        'redirect_uri': 'http://127.0.0.1:8000/auth/login/github/authorized',
        'state': 'git-stat'
    }
    url = 'https://github.com/login/oauth/access_token'
    response = requests.post(url, params)
    if response.status_code != 200:
        return "<h1>Access denied</h1>"
    content = response.content
    token = content.decode('utf-8').split('&')[0].split('=')[1]
    headers = {
        'Authorization': 'token ' + token,
        'Accept': 'application/vnd.github.v3+json'
    }
    url = 'https://api.github.com/user'
    response = requests.get(url, headers=headers)
    content = json.loads(response.content)
    user = {}
    for key, value in content.items():
        user[key] = value
        if key == 'login':
            return render_template('dashboard_blueprint.dashboard', username=value)

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
