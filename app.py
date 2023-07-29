from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome"



if __name__=='__main__':
    app.run(debug=True)