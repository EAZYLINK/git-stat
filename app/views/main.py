from flask import Blueprint, redirect, request, render_template, url_for
import sys, os, json
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_above = os.path.dirname(current_dir)
sys.path.append(folder_above)

main_blueprint = Blueprint('main_blueprint', __name__)

@main_blueprint.route('/home')
def index():
    return render_template('index.html')

@main_blueprint.route('/about')
def about():
    return render_template('about.html')

@main_blueprint.route('/contact')
def contact():
    return render_template('contact.html')

@main_blueprint.route('/signup')
def signup():
    return render_template('signup.html')

@main_blueprint.route('/login')
def login():
    if request.args.get('message'):
        message = request.args.get('message')
    else:
        message = ''
    return render_template('login.html', message=message)