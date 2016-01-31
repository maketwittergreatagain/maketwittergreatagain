# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1

from django.conf import settings
from .exceptions import NoTwitterToken


REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"


CONSUMER_KEY = settings.TWITTER['KEY']
CONSUMER_SECRET = settings.TWITTER['SECRET']


OAUTH_TOKEN = settings.TWITTER['TOKEN']
OAUTH_TOKEN_SECRET = settings.TWITTER['TOKEN_SECRET']


def get_oauth():
    oauth = OAuth1(
        CONSUMER_KEY,
        client_secret=CONSUMER_SECRET,
        resource_owner_key=OAUTH_TOKEN,
        resource_owner_secret=OAUTH_TOKEN_SECRET,
    )
    return oauth


def search_in_twitter(keywords):
    if not OAUTH_TOKEN:
        raise NoTwitterToken("You need to create and ``app`` en Twitter and add your keys to config.json")
    else:
        oauth = get_oauth()

    # https://api.twitter.com/1.1/search/tweets.json?q=cucaracha%20domino&mode=photos&result_type=popular
    payload = {
        'q': keywords,
        'mode': 'photos',
        'result_type': 'mixed',
        'count': 20,
    }
    url = "https://api.twitter.com/1.1/search/tweets.json"

    try:
        r = requests.get(url=url, auth=oauth, params=payload)
    except:
        print("Error")

    items = []
    data = r.json()
    for i in data['statuses']:
        item = None
        try:
            item = i['retweeted_status']
        except KeyError:
            pass

        if item is not None:
            if 'media' in item['entities']:
                tweet_id = item['id_str']
                image_urls = []
                for j in item['entities']['media']:
                    image_urls.append(j['media_url'])
                status = item['text']
                screen_name = item['user']['screen_name']
                retweet_count = item['retweet_count']
                items.append({
                    'tweet_id': tweet_id,
                    'image_urls': image_urls,
                    'status': status,
                    'screen_name': screen_name,
                    'retweet_count': retweet_count,
                })
    return items
