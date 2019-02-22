# When this file is run, it will put in motion the functions that will look at the mentions and tweet responses under two conditions
# 1. the tweet contains a keyword. The program will then respond with a phrase.
# 2. The tweet contains an image. The program will then respond with the image and a phrase.

# import everything we will need

import tweepy
from secrets import *
import time
from io import BytesIO
import requests
from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

# start an OAuthHandler Instance

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# definitions for functions that will store the tweet id of the last tweet that the bot saw
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


# def'n for the function that will respond to tweets

def reply_to_tweets(): #this function will automatically respond to tweets
    filename = 'yourimage.png'
    print('retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended',
                        include_entities=True) #this will set mentions equal to all mentions since the last seen mention
    print(mentions)
    for mention in reversed(mentions): #we reverse mentions so that we go through the tweets in chronological order
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if 'mention' in mention.full_text.lower(): # if statement for keyword
            print('found it!')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name +
                    ' I have seen your mention!', mention.id)
        else:
            print('no mention in that one')

        # print(mention.extended_entities)

        if 'media' in mention.entities:
            print('found an image')
            photo_URL = mention.entities['media'][0]['media_url']
            print(photo_URL)
                # download image
            request = requests.get(photo_URL, stream=True) # send a get request to get the image
            i = Image.open(BytesIO(request.content))
            i.save(filename)
            # Update status
            api.update_with_media(filename, status='@'+ mention.user.screen_name + ' Here is your image!',
                                  in_reply_to_status_id=mention.id)
            print('got the photo and replied!')
        else:
            print("no image here")

    print('all up to date!')

while True:
    reply_to_tweets()
    time.sleep(120)