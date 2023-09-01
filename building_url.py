from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def Welcome():
    return "Welcome to My web application"

@app.route('/fail/<int:score>')
def fail(score):
    return "The student fail the exam"

@app.route('/sucess/<int:score>')
def sucess(score):
    return "The student pass the exam"

@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks<50:
        result = 'fail'   # calling fail function
    else:
        result = 'sucess' # calling sucess function
    return redirect(url_for(result,score=marks)) # score is input of fail and sucess functions

if __name__ == "__main__":
    app.run(debug=True)