from flask import Flask, redirect, url_for

# WSGI Application
app=Flask(__name__)

# decorator param(rule, option)
@app.route('/')
def welcome():
    return 'Welcome to my Flask App!'

@app.route('/members')
def members():
    return 'This is my Flask App! Welcome Members!'

@app.route('/success/<int:score>')
def success(score):
    return "Sucess! (Score:  " + str(score) + " )"

@app.route('/failed/<int:score>')
def failed(score):
    return "Failed! (Score:  " + str(score) + " )"

# Result Checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks<50:
        result = 'failed'
    else:
        result = 'success'        
    # return result
    return redirect(url_for(result, score = marks))

if __name__=='__main__':
    # param(debug = bool)
    app.run(debug = True)

