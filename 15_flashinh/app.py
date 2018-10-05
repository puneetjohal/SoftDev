#Puneet Johal
#SoftDev1 pd7
#K15 -- Oh yes, perhaps I do...
#2018-10-03

from flask import Flask, render_template, request, session, url_for, redirect, flash
from os import urandom

app = Flask(__name__)
app.secret_key = urandom(32)

@app.route("/")
def disp_login():
    return render_template ('base.html')

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
        flash("Wrong password")
        return render_template ('base.html')

    elif (name != 'pjohal'):
        flash("Username does not exist")
        return render_template ('base.html')

    else:
        return "Something is wrong..."


if __name__ == "__main__":
    app.debug == True
    app.run()
