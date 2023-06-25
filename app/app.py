from flask import Flask, redirect, url_for
from views.users.route import user_blueprint
from views.auth.route import auth_blueprint
from views.main import main_blueprint 
from views.dashboard.route import dashboard_blueprint
import os
from dotenv import load_dotenv

load_dotenv()
PORT = os.getenv('PORT')

app = Flask("__name__")
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return redirect(url_for('main_blueprint.index'))

app.register_blueprint(user_blueprint, url_prefix='/user')
app.register_blueprint(auth_blueprint, url_prefix='/auth')
app.register_blueprint(main_blueprint, url_prefix='/')
app.register_blueprint(dashboard_blueprint, url_prefix='/dashboard')

if __name__ == "__main__":
    app.run(port=PORT, debug=True)
