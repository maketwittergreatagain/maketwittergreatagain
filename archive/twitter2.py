import requests
import json
import urllib2
import urllib
import argparse
import sys
import oauth2
import secret

#twitter
consumer_key = secret.TWITTER_KEY
consumer_secret = secret.TWITTER_SECRET
Access_Token = secret.ACCESS_TOKEN
Access_Token_Secret = secret.ACCESS_TOKEN_SECRET

search_url = 'https://api.twitter.com/1.1/search/tweets.json?q=%s&result_type=mixed&count=10'

getFullTweet = 'https://api.twitter.com/1.1/statuses/oembed.json?id={0}'

tweetlist = []
htmllist = []

#gets data in json form
def request(url):
    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    oauth_request = oauth2.Request(method="GET", url=url)

    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': Access_Token,
            'oauth_consumer_key': consumer_key
        }
    )
    token = oauth2.Token(Access_Token, Access_Token_Secret)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    conn = urllib2.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()
    return response

def putInList(data):
    for x in range(0, 5):
        if 'text' in data['statuses'][x]:
            status = data['statuses'][x]['text']
            if float(textSentiment(status)) < -0.5:
                tweetlist.append(data['statuses'][x]['id_str'])
    return tweetlist

def getIds():
    response = request(search_url)
    return putInList(response)

def getEmbed():
    tlist = getIds()
    for id in tlist:
        url = 'https://api.twitter.com/1.1/statuses/oembed.json?id={0}'.format(id)
        embed = request(url)
        htmllist.append(embed['html'])
    return htmllist


def textSentiment(status):
    ALCHEMY_URL = 'http://access.alchemyapi.com/calls/text/TextGetTextSentiment?apikey=%s&outputMode=json&text={0}' % secret.ALCHEMY_KEY
    tweettext = urllib.quote(status.encode('utf8'))
    textscore=0
    url = urllib2.urlopen(ALCHEMY_URL.format(tweettext))
    sentiment = json.loads(url.read())
    if 'score' in sentiment['docSentiment']:
        textscore = sentiment['docSentiment']['score']
    return textscore
