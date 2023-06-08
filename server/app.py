from flask import Flask, request

app = Flask("__name__")

@app.route('/')
def home():
    data = {}
    data["name"] = "Ezekiel"
    data["mat no"] = "ENG1703962"
    return data

@app.post('/api/v1/auth/signup')
def signup():
    data = request.values
    return data

@app.post('/api/v1/auth/login')
def login():
    data = request.values
    return (data['username'])




if __name__ == "__main__":
    app.run('127.0.0.1', 8000, debug=True)