## Integrate HTML with Flask
## HTTP verb GET AND POST

from flask import Flask,redirect,url_for,render_template,request
app = Flask(__name__)

@app.route('/')
def Welcome():
    return render_template('index.html')

## --------------------------------------------------##
@app.route('/fail/<int:score>')
def fail(score):
    res = ''
    if score <=50:
        res = 'Fail'
    else:
        res = 'Pass'
    return render_template('result.html',result=res)

@app.route('/sucess/<int:score>')
def sucess(score):
    res = ''
    if score <=50:
        res = 'Fail'
    else:
        res = 'Pass'
    return render_template('result.html',result=res) # result is variable which used in 'result.html'

##----------------------------------------------------##

## Result checker submit HTML page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method  == 'POST':
        science       = float(request.form['science'])
        maths         = float(request.form['maths'])
        c             = float(request.form['c'])
        datascience   = float(request.form['datascience'])
        total_score   = (science+maths+c+datascience) / 4
    res = ""
    if total_score<=50:
        res = 'sucess'
    else:
        res = 'fail'
    return redirect(url_for(res,score=total_score))


if __name__ == "__main__":
    app.run(debug=True)













    '''@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks<50:
        result = 'fail'   # calling fail function
    else:
        result = 'sucess' # calling sucess function
    return redirect(url_for(result,score=marks)) # score is input of fail and sucess functions
'''