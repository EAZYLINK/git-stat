from flask import Blueprint, redirect, request, render_template, session, url_for
import sys, os, json
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_above = os.path.dirname(current_dir)
sys.path.append(folder_above)
import requests
import matplotlib.pyplot as plt


dashboard_blueprint = Blueprint('dashboard_blueprint', __name__)

@dashboard_blueprint.route('/')
def view_dashboard():
    data = request.values
    session['username'] = data['username']
    return render_template('dashboard.html', username=data['username'])

@dashboard_blueprint.route('/repository')
def view_repository():
    if 'username' in session:
        return render_template('repository.html', username=session['username'])
    else:
        return render_template('login.html', message='Please login to continue')

def get_commit_count(owner, repo):
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/commits")
    if response.status_code == 200:
        commits = response.json()
        return len(commits)
    else:
        return 0

def get_issue_count(owner, repo):
    response = requests.get(f"https://api.github.com/repos/{owner}/{repo}/issues")
    if response.status_code == 200:
        issues = response.json()
        return len(issues)
    else:
        return 0
    
@dashboard_blueprint.route('/repository/search', methods=['GET'])
def fectch_repository_metrics():
    if 'username' in session:
        owner = session['username']
        repo = request.values['search_query']
        url = f"https://api.github.com/repos/{owner}/{repo}"
        headers = {
            'Accept': 'application/vnd.github.v3+json',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            stars = data['stargazers_count']
            commits = get_commit_count(owner, repo)
            issues = get_issue_count(owner, repo)
            forks = data['forks']
            commits_url = data['commits_url']
            issues_url = data['issues_url']
            create_at = data['created_at']
            updated_at = data['updated_at']

            plt.figure(figsize=(8, 4))
            plt.bar(['Stars', 'Forks'], [stars, forks])
            plt.xlabel('Metrics')
            plt.ylabel('Count')
            plt.title('Stars vs Forks')
            plt.savefig('static/stars_forks.png')

            # Create a line graph of commits and issues
            plt.figure(figsize=(8, 4))
            plt.plot(['Commits', 'Issues'], [commits, issues], marker='o')
            plt.xlabel('Metrics')
            plt.ylabel('Count')
            plt.title('Commits vs Issues')
            plt.savefig('static/commits_issues.png')

            return render_template('repository.html', search_query= owner, username=owner, name=repo, commits=commits, issues=issues, stars=stars, forks=forks,  created_at = create_at, updated_at = updated_at,
                                   commits_url=commits_url, issues_url=issues_url, stars_forks_image='/static/stars_forks.png', commits_issues_image='/static/commits_issues.png')
        else:
            return render_template('repository.html', username=owner, message='Repository not found')
    else:
        return render_template('login.html', message='Please login to continue')

@dashboard_blueprint.route('/commits')
def view_commits():
    if 'username' in session:
        owner = session['username']
        return render_template('commits.html', username=owner)
    else:
        return render_template('login.html', message='Please login to continue')
    
@dashboard_blueprint.route('/commits/search', methods=['GET'])
def fetch_commits_metrics():
    if 'username' in session:
        owner = session['username']
        repo_name = request.values['repo_name']
        commit_id = request.values['commit_id']
        url = f"https://api.github.com/repos/{owner}/{repo_name}/commits/{commit_id}"
        headers = {
            'Accept': 'application/vnd.github.v3+json',
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return render_template('commits.html', username=owner, repo_name=repo_name, commit_id=commit_id, commit_message=data['commit']['message'], commit_author=data['commit']['author']['name'], commit_date=data['commit']['author']['date'])
        else:
            return render_template('commits.html', username=owner, message='Commit not found')
    else:
        return render_template('login.html', message='Please login to continue')