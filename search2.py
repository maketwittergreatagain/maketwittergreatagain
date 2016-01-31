import tweepy
import secret

API_KEY = secret.TWITTER_KEY
API_SECRET = secret.TWITTER_SECRET

# Replace the API_KEY and API_SECRET with your application's key and secret.
auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print ("Can't Authenticate")
    sys.exit(-1)

# Continue with rest of code

import sys
import jsonpickle
import os
import json

query = "sports"

def search(query):
    JSONstring = ''
    maxTweets = 100 # Some arbitrary large number
    tweetsPerQry = 100  # this is the max the API permits
    fName = 'tweets.txt' # We'll store the tweets in a text file.
    # If results from a specific ID onwards are reqd, set since_id to that ID.
    # else default to no lower limit, go as far back as API allows
    sinceId = None
    # If results only below a specific ID are, set max_id to that ID.
    # else default to no upper limit, start from the most recent tweet matching the search query.
    max_id = -1L
    tweetCount = 0
    print("Downloading max {0} tweets".format(maxTweets))
    with open(fName, 'w') as f:
		while tweetCount < maxTweets:
			try:
				if (max_id <= 0):
					if (not sinceId):
						new_tweets = api.search(q=query, count=tweetsPerQry)
					else:
						new_tweets = api.search(q=query, count=tweetsPerQry, since_id=sinceId)
				else:
					if (not sinceId):
						new_tweets = api.search(q=query, count=tweetsPerQry, max_id=str(max_id - 1))
					else:
						new_tweets = api.search(q=query, count=tweetsPerQry, max_id=str(max_id - 1), since_id=sinceId)
				if not new_tweets:
					print("No more tweets found")
					break
                    for tweet in new_tweets:
                        f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
                    JSONstring.append(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
                tweetCount += len(new_tweets)
				print("Downloaded {0} tweets".format(tweetCount))
				max_id = new_tweets[-1].id
			except tweepy.TweepError as e:
				# Just exit if any error
				print("some error : " + str(e))
				break
	print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))
    return JSONstring

def getIds(tweets):
    jpy = json.loads(tweets)
    print jpy
    """
    id_list = []
    results = concept_expansion.get_results(job_id)
    #print(json.dumps(results, indent=2))
    json_dict = json.loads(json.dumps(results))
    for domain_dict in json_dict['return_seeds']:
        new_html.append(domain_dict['result']) #+= "%s\n" % domain_dict['result']
    return new_html
    """

jayson = search(query)
getIds(jayson)
