from flask import Flask

app = Flask("__name__")

@app.route('/')
def home():
    data = {}
    data["name"] = "Ezekiel"
    data["mat no"] = "ENG1703962"
    return data






if __name__ == "__main__":
    app.run(debug=True)