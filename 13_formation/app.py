from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def func():
    return render_template("woo.html")

if __name__ == "__main__":
    app.debug == True
    app.run()
