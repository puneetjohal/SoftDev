from flask import Flask, render_template
app = Flask(__name__)

@app.route("/templates")
def test():
    return render_template(
        'foo.html'
        )

app.run()

