from twython import Twython


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

def main():
	result = twitter.search(q='FOOTBALL')
	print result

if __name__ == "__main__":
	main()