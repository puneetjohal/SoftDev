import json, urllib.request, urllib.parse
from flask import Flask, render_template
app = Flask(__name__)

KEY = "10a55cbc-4834-4e19-966f-24a6679c9256"
URL_STUB = "http://version1.api.memegenerator.net//Generators_Select_ByPopular?pageIndex=0&pageSize=12&days=&apiKey="
URL = URL_STUB + KEY

@app.route("/")
def func():
    u = urllib.request.urlopen(URL)
    response = u.read()
    data = json.loads(response)
    #print(data)
    return render_template("index.html",
                           name = "Memes",
                           stuff = "",
                           img = data["result"][0]["imageUrl"],
                           allmeta = data)



if __name__ == "__main__":
    app.debug == True
    app.run()
