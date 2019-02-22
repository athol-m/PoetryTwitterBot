# PoetryTwitterBot
This repository will include files that describe my process and code for creating a poetry Twitter bot that will respond with poetry when a user tweets an image at the account. 

## Description of Files
### secrets.py
This file holds the "secrets" that are needed to initiate the 0AuthHandler request including all the access tokens. These are found on the app page for your Twitter developer account. By having these tokens in one file, it makes it easy to import the contents of the file into whatever project is being used so that 1) code can be shared without sharing private access codes and 2) so that the codes don't need to be added to every file that wishes to use them. 

### TweetWithPython.py
This note includes the code needed to create a function that runs continuously to search the timeline for mentions and respond to mentions including a keyword.

### last_seen_id.txt
This text file holds the Tweet ID of the last tweet that mentioned the account that the function analysed. 

### RespondWithImages.md
Using the Tweepy library, we will:
1. authenticate with Twitter
2. set up a stream
3. scan mentions for a keyword and respond with a phrase
4. scan mentions for an image and respond with the image and a phrase
5. run the function continuously
