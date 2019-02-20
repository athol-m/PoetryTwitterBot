# this file will contain the code that will let me tweet to my account using Python

# get everything we need
import tweepy # we'll use the streaming API to push messages to a persistent session
from RespondingTwitterBot.secrets import * # import the data within the file secrets.py
import time

### Let the program authenticate with Twitter
# create an OAuthHandler instance
# Twitter requires all requests to use OAuth for authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
# Construct the API instance which will be out entry point for operations we can perform with Twitter#
api = tweepy.API(auth) # create an API object


# now for the tweet:
# first, I will make a string that will hold the status update I want to post:
# statusupdate = "Now I can tweet using Python!"
# now the line of code that tweets it
# api.update_status(statusupdate)

# this code will store the twenty most recent mentions in a variable called "mentionsa"
mentions = api.mentions_timeline()
# to find out the type of data that is returned with this command:
type(mentions)
# and we see that it is <class 'tweepy.models.ResultSet'>
# ResultSet is like a list, so we can use indexing to find the first tweet
type(mentions[0]) # and we get <class 'tweepy.models.Status'>
# we see the mentions[0] is an object, and we can convert the object into a dictionary with the following
mentions[0].__dict__
#to see all of the keys used in the mention
the_keys = mentions[0].__dict__.keys()
print(the_keys)
# then to get the text from the tweet we can do:
the_text = mentions[0].text
print(the_text)

# Print the id and text of all mentions
for mention in mentions:
    print(str(mention.id) + ' -- ' + mention.text)
    if 'mention' in mention.text.lower():
        print('found it!')


# Now I will write definitions that will store the tweet id of the last tweet that the bot saw (so tweets aren't responded to twice)
FILE_NAME = 'last_seen_id.txt' # this makes it so I can easily write to the file

def retrieve_last_seen_id(file_name): #this function will retrieve the last seen id which is the text within the file
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name): #this function will edit the file and update it with the most recently seen tweet id
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return
# 1091036443257040898 for testing (id of first sample tweet)
id_text = 1091036443257040898
store_last_seen_id(id_text, FILE_NAME)
print(retrieve_last_seen_id(FILE_NAME)) #print it


def reply_to_tweets(): #this is the function that will automatically respond to tweets
    print('retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended') #this will set mentions equal to all mentions since the last seen mention
    for mention in reversed(mentions): #we reverse mentions so that we go through the tweets in chronological order
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if 'mention' in mention.full_text.lower():
            print('found it!')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name +
                    ' I have seen your mention!', mention.id)
    print('all up to date!')

while True:
    reply_to_tweets()
    time.sleep(120)