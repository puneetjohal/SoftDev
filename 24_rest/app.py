import Flask, render_template, json, urllib

@app.route("/")
def root():
    u = urllib.urlopen("link")
    response = u.read()
    data = json.loads(response)


if __name__ == "__main__":
    app.debug == True
    app.run()
