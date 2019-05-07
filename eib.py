# this file contains function definitions to do the following:
# 1. import an image from twitter.py
# 2. "analyse" the image
# 3. choose a seed word

import random
import PIL
from PIL import Image
from PIL import ImageFile

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
    if (R < 200 and R > G and G > B):           # each if statement will test to see into which category
        colorname = "brown"                     # the color at hand falls.
    elif (B >= 235 and G >= 235 and R >= 235):  # all RGB ranges are based on my own observations and testing.
        colorname = "white"
    elif (R >= 66 and R < 235) and ( B >= 66 and B < 235) and (G >= 66 and G < 235):
        colorname = "grey"
    elif (G <= 65 and B <= 65 and R <= 65):
        colorname = "black"
    elif (R == 255 and G < R and B < R) or (G == 0 and B == 0): # make more categories for orange and red
        colorname = "red"
    elif (R < 255 and R >= 20) and (R >= G and G >= B ) and (G != 0 and B != 0):
        colorname = "orange"
    elif (B < R and R == G):
        colorname = "yellow"
    elif (G == 255 and G>R and G>B) or (R == 0 and B == 0) or (G > B and G > R):
        colorname = "green"
    elif (B == 255 and G >= R) or (R == 0 and G == 0):
        colorname = "blue"
    elif (G == 0 and R != 0 and R == 0.5*B) or (G == 0 and R != 0 and R == 0.5*(B-1)) or (G == R and B >= R):
        colorname = "purple"
    else:
        print ("no color found")
        return;
    print (colorname)
    return colorname;

def most_frequent(List):
    result = max(set(List), key=List.count)     # this function was adapted from one I found online
    print ("printing the result")               # it will work for any input int, char, or string list
    print(result)
    return result

def word_to_list(colorword):     # this function will convert a given color to the color list
    if colorword == "red":
        return red
    elif colorword == "orange":
        return orange
    elif colorword == "yellow":
        return yellow
    elif colorword == "green":
        return green
    elif colorword == "blue":
        return blue
    elif colorword == "purple":
        return purple
    elif colorword == "brown":
        return brown
    elif colorword == "white":
        return white
    elif colorword == "grey":
        return grey
    elif colorword == "black":
        return black


def find_color_1(im, width, height):
    rgb_im = im.convert('RGB')              # convert image to RGB
    # Go through the image's pixels
    colors = []                             # initialize an empty list
    for i in range(width):
        for j in range(0, height//3):       # this height range is so that we only look at the bottom third for now
            p = rgb_im.getpixel((i, j))     # get the pixel we are looking at
            print("printing p")
            print(p)
            this_color = which_color(p[0],p[1],p[2])    # find what color it is
            print("printing this_color")
            print(this_color)
            colors.append(this_color)       # add the color to the list
    the_color = most_frequent(colors)       # find the most frequent color
    print("printing the_color")
    print(the_color)
    the_color_list = word_to_list(the_color) # convert the color to a seed word
    print(the_color_list)
    return the_color_list                    # return the seed word


# the next to functions do the same thing but for the other thirds of the photo
def find_color_2(im, width, height):
    rgb_im = im.convert('RGB')              # convert image to RGB
    # Go through the image's pixels
    colors = []                                  # this will be the index for the list of colors in the photo
    for i in range(width):
        for j in range((height//3)+1, 2*(height//3)):
            p = rgb_im.getpixel((i, j))
            print("printing p")
            print(p)
            this_color = which_color(p[0], p[1], p[2])
            print("printing this_color")
            print(this_color)
            colors.append(this_color)
        the_color = most_frequent(colors)
        print("printing the_color")
        print(the_color)
        the_color_list = word_to_list(the_color)
        print(the_color_list)
        return the_color_list

def find_color_3(im, width, height):
    rgb_im = im.convert('RGB')              # convert image to RGB
    # Go through the image's pixels
    colors = []                                    # this will be the index for the list of colors in the photo
    for i in range(width):
        for j in range((2*(height//3))+1,height):
            p = rgb_im.getpixel((i, j))
            print("printing p")
            print(p)
            this_color = which_color(p[0], p[1], p[2])
            print("printing this_color")
            print(this_color)
            colors.append(this_color)
        the_color = most_frequent(colors)
        print("printing the_color")
        print(the_color)
        the_color_list = word_to_list(the_color)
        print(the_color_list)
        return the_color_list

# defining the function that will randomly pick one of the associated seed words from the color category vector entered as input
def pick_a_word(color):
    number = 0
    length = len(color)
    for x in range(1):                              # pick one number
        number = random.randint(0,length-1)         # in the range 0 - length-1 (number will be used as an index)
    word = color[number]
    print("printing word")
    print(word)
    return word;


# everything after this is for testing the functions
if __name__ == "__main__": # this idiom is useful so that when importing this file, anything after this line won't be run
# testing which_color
    which_color(50, 50, 50)
# testing the most frequent function
    testlist = "dog", "cat", "cat", "goose"
    most_frequent(testlist)

