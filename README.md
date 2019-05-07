# PoetryTwitterBot
This repository will include files that describe my process and code for creating a poetry Twitter bot that will respond with neural network generated poetry when a user tweets an image at the account. 

# Description of Files

## Files Currently in Use in the Project

### Main Program Files

#### twitter.py
This file contains the code that will 
1. authenticate with twitter
1. set up a stream and look for mentions
1. download an image from a mention
1. import lines of poetry from rnn.py 
1. tweet a reply to the user including their image and three lines of poetry

#### eib.py
The "everything in between" file, this is the file in which the image analysis and seed word generation is done. This file is stil *very much* a work in progress. Once completed, it will include a function that turns an image into three seed words by breaking the image into thirds, finding the most used color in each third, and then using the color to come up with a seed word by randomly selecting from a list of color association words that is specific to color associations for each color according to ideals and ideas in Western culture. 

#### rnn.py
This file *will* contain the parameters for the recurrent neural network that write the poetry and the function that takes a color and "turns it into" a seed word. But right now it only contains some sample variables so I can test the code in twitter.py. 


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


### Other Miscellaneous Files that I've Used Along the Way

#### RespondWithImages.md
This is a useful file that explains the OAuth process and simple handling of tweet attributes using Tweepy. 
Using the Tweepy library, we will:
1. authenticate with Twitter
2. set up a stream
3. scan mentions for a keyword and respond with a phrase
4. scan mentions for an image and respond with the image and a phrase
5. run the function continuously
