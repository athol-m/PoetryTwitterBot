# this file is a program that authenticates with my account and prints the tweets that the account has publically tweeted


# Import everything we will need

import tweepy # we'll use the streaming API to push messages to a persistent session
from secrets import * # import the data within the file secrets.py

### Let the program authenticate with Twitter
# create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
# Construct the API instance which will be out entry point for operations we can perform with Twitter#
api = tweepy.API(auth) # create an API object

# Print public tweets:
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)