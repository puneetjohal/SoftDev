import json, urllib.request, urllib.parse
from flask import Flask, render_template
app = Flask(__name__)

KEY = ""
URL_STUB = "https://api.pokemontcg.io/v1/cards"
URL = URL_STUB + KEY

@app.route("/")
def func():
    u = urllib.request.urlopen(URL)
    response = u.read()
    data = json.loads(response)
    #print(data)
    return render_template("index.html",
                           name = "Pokemon",
                           stuff = "",
                           img = "",
                           allmeta = data)



if __name__ == "__main__":
    app.debug == True
    app.run()
