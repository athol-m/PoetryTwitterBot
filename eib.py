# this file will do the following:
# 1. import an image from twitter.py
# 2. analyse the image
# 3. choose a seed word

import random
# from twitter import filename
# image = filename

word1 = 'yes'
word2 = 'yes'
word3 = 'yes'

# Defining the lists for each color category that will hold the possible seed words
red = ["fire", "hot", "anger", "angry", "mad", "apple", "candy", "stop", "passion", "celebration", "evil", "caution", "prosperity", "luck", "energy", "desire"]
orange = ["fire", "harvest", "autumn", "citrus", "warmth", "courage", "gluttony"]
yellow = ["happy", "sun", "golden", "blonde", "bright", "warmth", "hospitality", "taxi", "school bus", "gold", "happiness"]
green = ["grass", "money", "go", "good", "greed", "envy", "jealous", "luck", "nature", "Earth", "youth", "military", "hope", "growth"]
blue = ["ocean", "water", "sad", "sorrow", "glum", "cold", "trust", "authority", "masculine", "boy", "calm", "trust"]
purple = ["pride", "lavender", "royaly", "wealth", "fame", "honor", "imagination"]
brown = ["dirt", "Earth", "dirty", "health", "barren", "stable", "wholesome", "grains", "comfort", "neutral"]
white = ["purity", "clean", "virginity", "surrender", "marriage", "peace", "hospital", "holy", "truce"]
grey = ["gloomy", "dreary", "clouds", "ominous", "impartial", "detached"]
black = ["darkness", "unknown", "mystery", "finality", "death", "force", "control", "magic"]

# Defining the function that tells us into which color category the RGB code falls
def which_color(R,G,B):
    if (R == 255 & G <= R & B <= R) or (G == 0 & B == 0):
        colorname = red
    elif (R < 255 & R >= 200 & R >= G & G >= B & G != 0 & B != 0):
        colorname = orange
    elif (B < R & R == G):
        colorname = yellow
    elif (G == 255) or (R == 0 & B == 0) or (G > B & G > R):
        colorname = green
    elif (B == 255 & G >= R) or (R == 0 & G == 0):
        colorname = blue
    elif (G == 0 & R != 0 & R == 0.5*B) or (G == 0 & R != 0 & R == 0.5*(B-1)) or (G == R & B >= R):
        colorname = purple
    elif (R < 200 & R > G & G > B):
        colorname = brown
    elif (R == G & G == B & R >= 195):
        colorname = white
    elif (R == G & G == B & R >= 66 & R <= 194):
        colorname = grey
    elif (R == G & G == B & R <= 65):
        colorname = black
    else:
        print ("no color found")
        return;
    print (colorname)
    return colorname;

# defining the function that will randomly pick one of the associated seed words from the color category vector entered as input
def pick_a_word(color):
    number = 0
    length = len(color)
    for x in range(1):                              # pick one number
        number = random.randint(0,length-1)         # in the range 0 - length-1 (number will be used as an index)
    word = color[number]
    return word;

# def'n for function to go from one complete image to three seed words ----- just testing this for now
# steps of the function
# 1. split image into thirds
# 2. identify most used color in each third
# 3. pick seed word for each third
def image_to_seeds(color):
    global word1, word2, word3
    word1 = pick_a_word(color)
    return

image_to_seeds(green)
print(word1)
