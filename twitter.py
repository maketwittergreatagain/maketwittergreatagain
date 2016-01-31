from twython import Twython
import json
import requests
from requests_oauthlib import OAuth1
import secret
from auth import (
	consumer_key,
	consumer_secret,
	access_token,
	access_token_secret,
	)

twitter = Twython(secret.TWITTER_KEY,
	secret.TWITTER_SECRET,
	secret.ACCESS_TOKEN,
	secret.ACCESS_TOKEN_SECRET)

def search(query):
    result = twitter.search(q=query)
    length = len(result['statuses'])
    new_list = [result['statuses'][i]['id'] for i in range(length)]
    print new_list
    return new_list

"""
def embed(tweet_ids):
    new_html = []
    for tweet in tweet_ids:
        results = "https://api.twitter.com/1.1/statuses/oembed.json?id=%s" % tweet
        json_dict = json.loads(json.dumps(results))
        print json_dict
        for x in json_dict:
            new_html.append(x[0])
    return new_html
"""

def get_oauth():
    oauth = OAuth1(
        secret.TWITTER_KEY,
        client_secret = secret.TWITTER_SECRET,
        resource_owner_key = secret.ACCESS_TOKEN,
        resource_owner_secret = secret.ACCESS_TOKEN_SECRET,
    )
    return oauth

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def get_embedded_tweets(tweet_ids):
    embedded_tweets = []
    oauth = get_oauth()
    for id in tweet_ids:
        url = 'https://api.twitter.com/1.1/statuses/oembed.json'
        payload = {
            'id': id,
        }
        r = requests.get(url=url, auth=oauth, params=payload)
        r = r.json()
        print "r: %s\n" % r
        tweet = r['html']
        print "tweet: %s\n" % tweet
        embedded_tweets.append(tweet)
        #embedded_tweets = byteify(embedded_tweets)
    print embedded_tweets
    return embedded_tweets


#get_embedded_tweets(search("sports"))
