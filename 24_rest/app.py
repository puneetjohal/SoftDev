import json, urllib.request, urllib.parse
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def func():
    u = urllib.request.urlopen("https://api.nasa.gov/planetary/apod?api_key=MrEGd06mQpt76yu7K4MRWHdg47cqQCG3jl6d0QHO")
    response = u.read()
    data = json.loads(response)
    #print(data)
    return render_template("index.html",
                           img = data['url'],
                           explain = data['explanation'],
                           allmeta = data)



if __name__ == "__main__":
    app.debug == True
    app.run()
