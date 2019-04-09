# When this file is run, it will put in motion the functions that will look at the mentions and tweet responses
#   after passing information to and receiving information from other files

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

# defining global variables
filename = 'yourimage.png'
last_seen_id = retrieve_last_seen_id(FILE_NAME)

# def'n for function that will download and output the image tweeted at the account
def dwn_img():
    global filename
    filename = 'yourimage.png'
    print('retrieving tweets...')
    global last_seen_id
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    print('last seen id is: ')
    print(last_seen_id)
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended',
                        include_entities=True) #this will set mentions equal to all mentions since the last seen mention
    print(mentions)
    for mention in reversed(mentions): #we reverse mentions so that we go through the tweets in chronological order
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)

        if 'media' in mention.entities:
            print('found an image')
            photo_URL = mention.entities['media'][0]['media_url']
            print(photo_URL)
                # download image
            request = requests.get(photo_URL, stream=True) # send a get request to get the image
            i = Image.open(BytesIO(request.content))
            i.save(filename)
            print('got the photo!')
            return # I return here so that it only works on a single mention at a time
        else:
            print("no image here")
            return


# import rnn file and set it to global variables
import rnn

line1 = rnn.line1
line2 = rnn.line2
line3 = rnn.line3

print('printing the poetry...')
print(line1 + '\n' + line2 + '\n' + line3)

# def'n for function that will tweet the image and lines of poetry
def tweet_img():
    print('sending poetry and image...')
    global last_seen_id, filename, line1, line2, line3
    api.update_with_media(filename, status='@'+ mention.user.screen_name + '\n' + line1 +'\n'+line2+'\n'+line3,
                                    in_reply_to_status_id=last_seen_id)

while True:
    dwn_img()
    time.sleep(150)

### run up to this point with no error codes
# but after the first time, the sample imports from rnn don't print. Not sure why.