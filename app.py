from flask import Flask, render_template, request, session
import concepts, search2, secret
from flask.ext.twitter_oembedder import TwitterOEmbedder
from flask.ext.cache import Cache

twitter_oembedder = TwitterOEmbedder()

app = Flask(__name__)
cache = Cache(app)

twitter_oembedder.init(app,cache)

# CONFIG

app.config['TWITTER_CONSUMER_KEY'] = "b7YJCQN3XYOvxIevp1o5mc684"
app.config['TWITTER_CONSUMER_SECRET'] = "cEDvjmnGl1KbnbwEW8v5hjPXWnIRnwm2FNuS9L0SkFfhiYQYQD"
app.config['TWITTER_ACCESS_TOKEN'] = "3090270271-VzR6iBYUGdM69zan3WJ8OhApGLtZmjijxUNeDeL"
app.config['TWITTER_TOKEN_SECRET'] = "PCIlN6jPIxuhwMlS1eOW7i7fQo14WFqVhsGqa7AidFHBv"

@app.route('/', methods=["GET", "POST"])
def index():
    if (request.method == "GET"):
        return render_template("index.html")
    elif (request.form['search'] != "" and request.method == "POST"):
        query = request.form['search']
        tweets = search2.
        results = concepts.getConcepts(query)
        return render_template("index.html", keyword_list=results, query=query, tweets=tweets)


if __name__=="__main__":
    app.debug = True
    #app.secret_key = "no way"
    app.run(host='0.0.0.0', port=8000)
