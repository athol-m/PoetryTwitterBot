# When this file is run, it will put in motion the functions that will look at the mentions and tweet responses
#   after passing information to and receiving information from other files

# import everything we will need
import tweepy
from secrets import *
import time
from io import BytesIO
import requests
from rnn import *
from eib import *
ImageFile.LOAD_TRUNCATED_IMAGES = True

# start an OAuthHandler Instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# definitions for functions that will store the tweet id of the last tweet that the bot saw
FILE_NAME = 'last_seen_id.txt'  # this makes it so I can easily write to the file
def retrieve_last_seen_id(file_name):  # this function will retrieve the last seen id which is the text within the file
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id,
                       file_name):  # this function will edit the file and update it with the most recently seen tweet id
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

# defining global variables
filename = 'yourimage.png'
last_seen_id = retrieve_last_seen_id(FILE_NAME)

# def'n for function that will download the image tweeted at the account
def dwn_img():
    global filename                     # bring in those global variables
    filename = 'yourimage.png'
    print('retrieving tweets...')
    global last_seen_id
    last_seen_id = retrieve_last_seen_id(FILE_NAME)        # get the last seen tweet id to start working with the tweet
    print('last seen id is: ')
    print(last_seen_id)
    mentions = api.mentions_timeline(
                           last_seen_id,
                           tweet_mode='extended',
                        include_entities=True) #this will set mentions equal to all mentions since the last seen mention
    print(mentions)
    for mention in reversed(mentions): #we reverse mentions so that we go through the tweets in chronological order
        last_seen_id = mention.id


        if 'media' in mention.entities:
            print('found an image')
            photo_URL = mention.entities['media'][0]['media_url']
            print(photo_URL)
            # download image:
            request = requests.get(photo_URL, stream=True) # send a get request to get the image
            i = Image.open(BytesIO(request.content))
            i.save(filename)
            print('got the photo!')
            return # I return here so that it only works on a single mention at a time
        else:
            print("no image here")
            return


# def'n for function that will tweet the image and lines of poetry
def tweet_img(filename, line1, line2, line3):       # input the image filename and the 3 lines to be tweeted
    print('sending poetry and image...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME) # we get the last seen id so we can reply directly to the submitter's tweet
    print(last_seen_id)
    mentions = api.mentions_timeline(
                           last_seen_id,
                           tweet_mode='extended',
                        include_entities=True) #this will set mentions equal to all mentions since the last seen mention
    for mention in reversed(mentions): #we reverse mentions so that we go through the tweets in chronological order
        last_seen_id = mention.id
        # now update the status with the image and the lines of poetry
        api.update_with_media(filename, status= '@'+ mention.user.screen_name + '\n' + line1 +'\n'+line2+'\n'+line3,
                                            in_reply_to_status_id=last_seen_id)
    store_last_seen_id(last_seen_id, FILE_NAME)
    return

# this function will resize the submitted image so that it is more easily analysed
def resizing():
    image = Image.open('yourimage.png')     # open the image
    width, height = image.size              # get the size
    print(width, height)
    newheight = 302.0
    newwidth = 403.0
    y = newheight/height
    x = newwidth/width                      # this is so that we get a specific resolution and image size
    print(x, y)
    image.resize((int(width*x),int(height*y)))  # then we resize the image
    return image


# this is the function that does everything. It combines all the pieces and does the work.
def ball_rolling():
    dwn_img()

    newimage = resizing()

    color1 = find_color_1(newimage, newimage.width, newimage.height)
    color2 = find_color_2(newimage, newimage.width, newimage.height)
    color3 = find_color_3(newimage, newimage.width, newimage.height)

    seed1 = pick_a_word(color1)
    seed2 = pick_a_word(color2)
    seed3 = pick_a_word(color3)

    line1 = seed_to_line(seed1, file="line1.txt")
    line2 = seed_to_line(seed2, file="line2.txt")
    line3 = seed_to_line(seed3, file="line3.txt")

    tweet_img(filename, line1, line2, line3)


# we have two options for running the code.
#we can either just run the function once:
ball_rolling()

# or we can have an infinite while loop and the code will be run every 150 seconds
#while True:
 #   time.sleep(150)


