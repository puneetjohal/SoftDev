#Puneet Johal
#SoftDev1 pd7
#K13 -- Echo Echo Echo . . .
#2018-09-28
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def redirect():
    return render_template ('woo.html')

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    print(request.args)
    name = request.args['username']
    meth = request.method
    return '<h3> Have a blessed day, ' + name + '</h3> <br> Request method used: ' + meth

if __name__ == "__main__":
    app.debug == True
    app.run()
