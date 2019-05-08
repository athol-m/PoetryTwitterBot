# PoetryTwitterBot
This repository will include files that describe my process and code for creating a poetry Twitter bot that will respond with neural network generated poetry when a user tweets an image at the account. 

# Description of Files

## Files Currently in Use in the Project

### Main Program Files

#### twitter.py
This file contains the code that will 
1. import functions from eib.py and rnn.py to analyze images and generate text
1. authenticate with twitter
1. set up a stream and look for mentions
1. download an image from a mention
1. tweet a reply to the user including their image and three lines of poetry

#### eib.py
The "everything in between" file, this is the file that includes definitions for all things that aren't twitter or rnn related. 
So the functions and things that are defined here are:
1. defines the lists of seed words associated with each color
1. defines the function that turns an RGB value into a color category
1. most_frequent: this function finds the most frequent occurance in a list
1. word_to_list: this function convert the color category word into the color category list
1. find_color_1, find_color_2, find_color_3: these functions will look at a specified third of the image and figure out the most used color in the third of the image
1. pick_a_word: converts a color list into a seed word by randomly selecting one of the words in the color word list

The list of color association words is based off of single-word associations with those colors in Western culture. The information was aggregated from my own experience as well as some online blogs and sources that speak about color associations. 

#### rnn.py
This file contains the parameters for the recurrent neural network that write the poetry and the function. It also includes two functions:
1. seed_to_line: this function will generate 250 characters of poetry to a file based on an inputted seed word. Then, it trims the results to a single line that is returned.  
1. trim_results: this is the function that will trim the 250 character generation into a single line.

#### 200chartweet.py
This is an independent program file that, when run, will tweet 200 characters of poetry generated on the spot. 

### Other Files Used (not all are included in this repository)

#### secrets.py
This file holds the "secrets" that are needed to initiate the 0AuthHandler request including all the access tokens. These are found on the app page for your Twitter developer account. By having these tokens in one file, it makes it easy to import the contents of the file into whatever project is being used so that 1) code can be shared without sharing private access codes and 2) so that the codes don't need to be added to every file that wishes to use them. 

#### last_seen_id.txt
This text file holds the Tweet ID of the last tweet that mentioned the account that the function analysed. 

#### yourimage.png
This is the image that was most recently submitted and responded to. It gets replaced with a new image for each mention. 

#### line1.txt, line2.txt, line3.txt
These are the files into which the generated poetry will be written. 

#### poetry5_config.json
This file contains configuration perameters for the neural network including whether the generation is line delimited. 

#### poetry5_weights.json
This json file contains the weights and probabilities textgenrnn uses to predict the next character and generate the poetry. 

#### poetry5_vocab.json
This is the vocabulary the RNN draws from. 


### Other Somewhat Miscellaneous Files

#### Using a virtualenv.md
This markdown file includes why I chose to run my programs for this project using a ```virtualenv``` as well as how I set one up and use it. 

#### RespondWithImages.md
This is a useful file that explains the OAuth process and simple handling of tweet attributes using Tweepy. 
Using the Tweepy library, we will:
1. authenticate with Twitter
2. set up a stream
3. scan mentions for a keyword and respond with a phrase
4. scan mentions for an image and respond with the image and a phrase
5. run the function continuously
