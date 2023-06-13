from flask import Blueprint, request, render_template
import sys, os, json
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_above = os.path.dirname(current_dir)
sys.path.append(folder_above)


dashboard_blueprint = Blueprint('dashboard_blueprint', __name__)

@dashboard_blueprint.post('/dashboard')
def view_dashboard():
    data = request.values
    return render_template('dashboard.html', username=data['username'])
