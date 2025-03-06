from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hellow world"

@app.route("/yay/")
def yay():
    return "HEHEHEHEHEH"

@app.route("/yessir")
def oiahdoshdas():
    return render_template("hehe.html")


if __name__ == '__main__':#Why though :(
    app.run()
    
