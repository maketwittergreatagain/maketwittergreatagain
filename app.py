from flask import Flask, render_template, request, session
import concepts, twitter, secret

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if (request.method == "GET"):
        return render_template("index.html")
    else:
        query = request.form['search']
        twitter_results = twitter.search(query)
        tweets = twitter.get_embedded_tweets(twitter_results)
        results = concepts.getConcepts(query)
        return render_template("index.html", keyword_list=results, query=query, tweets=tweets)

if __name__=="__main__":
    app.debug = True
    #app.secret_key = "no way"
    app.run(host='0.0.0.0', port=5000)
