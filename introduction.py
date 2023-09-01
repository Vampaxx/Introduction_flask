from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my Web application. This is my beggining.I have new"

@app.route('/home_page')
def homepage():
    return "Welcome to Home page"

@app.route('/workspace')
def workspace():
    return "workspace"
if __name__ == "__main__":
    app.run(debug=True)