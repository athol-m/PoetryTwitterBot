# Responding to Mentions and Tweeting Images
The code in this file is the main program file for a program that, when run, will stream the authenticated Twitter feed to look for mentions, assess mentions for keywords or images, then respond with either a phrase or the image and a phrase. 

Doing this requires that you have a [developer Twitter account](https://developer.twitter.com/en/apply-for-access.html) and have created a [Twitter app](https://developer.twitter.com/en/apps) for your project.

### Other files referenced by this program:
[**secrets.py**](https://github.com/athol-m/PoetryTwitterBot/blob/master/secrets.py) which holds the authentication tokens for the Twitter account

[**last_seen_id.txt**](https://github.com/athol-m/PoetryTwitterBot/blob/master/last_seen_id.txt) which holds the Tweet ID of the tweet the program most recently saw

Both of these files can be seen in my PoetryTwitterBot respository but they serve as examples: the values have been removed (to protect personal data)

## Import the needed libraries and data
```python
import tweepy
from secrets import *
import time
from io import BytesIO
import requests
from PIL import Image
from PIL import ImageFile
```

## Start an OAuth Handler instance
```python
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
```

## Other things to run now
```python
ImageFile.LOAD_TRUNCATED_IMAGES = True
FILE_NAME = 'last_seen_id.txt'
```

## Functions to store and reference the last seen tweet ID. 
```python
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
```

## The main function
The below function definition is the only function that the program will run and it has 2 if statements
1. if there is a keyword, give a stock response
2. if there is an image, save the image, reply with the image and a stock response

```python

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

        if 'media' in mention.entities: # if statement for media
            print('found an image')
            photo_URL = mention.entities['media'][0]['media_url']
            print(photo_URL)
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
    
```
## Running the function
The code below will allow the function to run continuously, and the function will run every 120 seconds
```python
while True:
    reply_to_tweets()
    time.sleep(120)
```
