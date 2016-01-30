from flask import Flask, render_template, request, session

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.debug = True
    app.secret_key = "no way"
    app.run(host='0.0.0.0', port=8000)
