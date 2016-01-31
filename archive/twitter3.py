import requests
from requests_oauthlib import OAuth1

def extract_ids(self):
    ids = []
    for tweet in self.memes:
        ids.append(tweet['tweet_id'])
    self.tweet_ids = ids

def get_oauth():
    oauth = OAuth1(
        secret.TWITTER_KEY,
        client_secret = secret.TWITTER_SECRET,
        resource_owner_key = secret.ACCESS_TOKEN,
        resource_owner_secret = secret.ACCESS_TOKEN_SECRET,
    )
    return oauth

def get_embeded_tweets(self):
    embeded_tweets = []
    oauth = get_oauth()
    for id in self.tweet_ids:
        url = 'https://api.twitter.com/1.1/statuses/oembed.json'
        payload = {
            'id': id,
        }
        r = requests.get(url=url, auth=oauth, params=payload)
        r = r.json()
        tweet = r['html']
        embeded_tweets.append(tweet)
        #final_url = urllib.unquote(url).decode('utf8')
    return embeded_tweets.encode('utf-8') #final_url
