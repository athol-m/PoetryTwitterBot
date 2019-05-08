# Why use a ```virtualenv```?
For this project, I created and used a ```virtualenv``` to run my programs. 

This is because my laptop is running Python 2.7 but I needed Python 3.6. 
Rather than interfering with my computer's Python file structure, 
I created a virtual environment in which I installed Python 3.6 as well as other packages and libraries
including ```textgennrnn```, ```tensorflow```, ```pillow```, and ```tweepy```. 
By creating a ```virtualenv```, I also have the benefit of installing packages to the environment rather than including
the install in my scripts. This makes running scripts a little smoother (in my opinion). 

# How I set up my ```virtualenv```

### A little bit about my system first:
I'm using a 2014 Macbook Air running MacOS 10.13.1 (High Sierra). (And yes, I know I need to update my OS)

### Installing virtual env
In terminal, run the following command:

```sudo pip install virtualenv```

If you run into any challenges, try running the following command:

```sudo easy_install pip```

### Now setting up a virtualenv
First, I created a directory for my Python work with the file path:
```~/Users/mathol/Python```

```mkdir Python && cd Python```

once in the directory, I made a virtualenv named ```env```:

```virtualenv env```

and activated it:

```source env/bin/activate```

Then I can install packages and run programs and use terminal normally. But any install is local and applied only to ```env```. Once I am finished, I deactivate it:

```deactivate```
