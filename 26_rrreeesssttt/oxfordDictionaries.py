import json, urllib.request, urllib.parse
from flask import Flask, render_template
app = Flask(__name__)

app_id = '507e6a25'
app_key = 'b10c0e930b62b9731b0ba009fa0b4b1a'

language = 'en'
word_id = 'Ace'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

#r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

@app.route("/")
def func():
    u = urllib.request.urlopen(url)
    response = u.read()
    data = json.loads(response)
    #print(data)
    return render_template("index.html",
                           name = "Oxford Dictionaries",
                           #stuff = response[0],
                           #img = response[1],
                           allmeta = data
                           )



if __name__ == "__main__":
    app.debug == True
    app.run()
