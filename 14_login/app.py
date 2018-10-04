#Puneet Johal
#SoftDev1 pd7
#K13 -- Do I Know You?
#2018-10-02

from flask import Flask, render_template, request, session, url_for, redirect
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(32)

@app.route("/")
def disp_login():
    return render_template ('form.html', error = '')

@app.route("/auth", methods = ["POST"])
def authenticate():
    #print url_for("disp_login") # Should print out "/"
    #print url_for("authenticate") # Should print out "/auth"
    #return redirect(url_for("disp_login")) # Redirects user to the url that is tied to the function "disp_login"

    name = request.form['username']
    password = request.form['password']

    if (name == 'pjohal' and password == 'pass'):
        session['name'] = name;
        return render_template ('loggedIn.html', returl = url_for("disp_login"))

    elif (name == 'pjohal' and password != 'pass'):
        return render_template ('form.html', error = 'Wrong password')

    elif (name != 'pjohal'):
        return render_template ('form.html', error = "Username doesn't exist")

    else:
        return "Something is wrong..."


if __name__ == "__main__":
    app.debug == True
    app.run()
