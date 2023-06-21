from flask import Blueprint, request, render_template, session
import sys, os, json
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_above = os.path.dirname(current_dir)
sys.path.append(folder_above)
import requests


dashboard_blueprint = Blueprint('dashboard_blueprint', __name__)

@dashboard_blueprint.route('/')
def view_dashboard():
    data = request.values
    return render_template('dashboard.html', username=data['username'])

@dashboard_blueprint.route('/repository')
def view_repository():
    if 'username' in session:
        return render_template('repository.html', username=session['username'])
    else:
        return render_template('login.html', message='Please login to continue')

@dashboard_blueprint.route('/repository/search_query')
def fectch_repository_metrics(owner, repo):
    owner = session['username']
    repo = request.values['repo']
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        stars = data['stargazers_count']
        forks = data['forks_count']
        commits = data['commits_url']
        issues = data['issues_url']
        return {
            'stars': stars,
            'forks': forks,
            'commits': commits,
            'issues': issues
        }
    else:
        return {
            'stars': 0,
            'forks': 0,
            'commits': 0,
            'issues': 0
        }
