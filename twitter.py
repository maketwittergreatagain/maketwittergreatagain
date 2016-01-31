from twython import Twython
import json
from auth import (
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret,
	)

twitter = Twython(consumer_key,
	consumer_secret,
	access_token,
	access_token_secret)

def search(query):
    result = twitter.search(q=query)
    length = len(result['statuses'])
    new_list = [result['statuses'][i]['id'] for i in range(length)]
    print new_list
    return new_list

def embed(tweet_ids):
    new_html = []
    for tweet in tweet_ids:
        results = "https://api.twitter.com/1.1/statuses/oembed.json?id=%s" % tweet
        json_dict = json.loads(json.dumps(results))
        print json_dict
        for x in json_dict:
            new_html.append(x[0])
    return new_html

embed(search("sports"))
