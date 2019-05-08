
# import everything we will need
import tweepy
from secrets import *
import time
from io import BytesIO
from textgenrnn import textgenrnn

# start an OAuthHandler Instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Defining our neural network
textgen = textgenrnn(weights_path='poetry5_weights.hdf5',
                vocab_path='poetry5_vocab.json',
                config_path='poetry5_config.json')

# Generate Poetry
def make_poetry(file):
    n = 1                                               # we are making one generation
    max_gen_length = 200                                # generates 200 characters
    textgen.generate_to_file(file, temperature=0.8,     # this is a function within textgenrnn
                         n=n,
                         max_gen_length=max_gen_length)
    f_read = open(file, 'r')                            # the text is generated to a file, so first we open the file
    file_text = f_read.read().strip()                   # then we add the text to a variable we can work with easily
    f_read.close()                                      # and close the file
    return file_text



# Tweet the poetry
file = '200char_gen.txt'
def tweet_em():
    output = make_poetry(file)
    print(output)
    api.update_status(status = "200 characters of generated poetry:" + '\n' + output)
    return


#Running it
tweet_em()
