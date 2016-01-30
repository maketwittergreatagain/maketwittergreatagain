from flask import Flask, render_template, request, session
import concepts

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if (request.method == "GET"):
        return render_template("index.html")
    else:
        query = request.form['search']
        #query = "sports"
        results = concepts.getConcepts(query)
        return render_template("index.html", keywords=results)


if __name__=="__main__":
    app.debug = True
    app.secret_key = "no way"
    app.run(host='0.0.0.0', port=8000)
