from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello1():
    return 'Yo hablo queso. <a href = "/2"> 还有谁? </a>'

@app.route("/2")
def hello2():
    return'Tu hablas queso. <a href = "/3"> 还有谁? </a>'

@app.route("/3")
def hello3():
    return 'Nosotros hablamos queso. <a href = "/2"> 还有谁? </a>'

if __name__ == "__main__":
    app.debug == True
    app.run()
