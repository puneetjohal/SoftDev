import json, urllib.request, urllib.parse
from flask import Flask, render_template
app = Flask(__name__)

KEY = "1b360549a76a42569bd961be7e567f35"
URL_STUB = "https://api.nytimes.com/svc/topstories/v2/home.json?api-key="
URL = URL_STUB + KEY

@app.route("/")
def func():
    u = urllib.request.urlopen(URL)
    response = u.read()
    data = json.loads(response)
    #print(data)
    return render_template("index.html",
                           stuff = data['results'][0]['title'],
                           abs = data['results'][0]['abstract'],
                           link = data['results'][0]['url'],
                           allmeta = data)



if __name__ == "__main__":
    app.debug == True
    app.run()
