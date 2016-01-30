from flask import Flask, render_template, request, session
import concepts

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if (request.method == "GET"):
        return render_template("index.html")
    elif (request.form['search'] != ""):
        query = request.form['search']
        results = concepts.getConcepts(query)
        return render_template("index.html", keyword_list=results)


if __name__=="__main__":
    app.debug = True
    app.secret_key = "no way"
    app.run(host='0.0.0.0', port=8000)
