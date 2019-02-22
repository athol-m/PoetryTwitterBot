## This is a markdown file for the code in the main file program file


'''python

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
    
'''
