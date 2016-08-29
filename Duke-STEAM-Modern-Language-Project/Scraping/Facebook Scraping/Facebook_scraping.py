'''
Created on Mar 7, 2016
Facebook scraping test
@author: lucy
'''


import facebook # You need to download the python for facebook SDK: https://github.com/pythonforfacebook/facebook-sdk
# I can help if you need it. But basically what you need to do is extract the zip folder into the python libraries folder. 
# I have an Anaconda interpreter, so I put this folder into the Anaconda library folder. 
import requests


def some_action(post):
    """ Here you might want to do something with each post. E.g. grab the
    post's message (post['message']) or the post's picture (post['picture']).
    In this implementation we just print the post's created time.
    """
    print(post['created_time'])


# Get a temporary access token
# here: https://developers.facebook.com/tools/explorer/
# You will need to make an app by becoming a facebook app developer: https://developers.facebook.com/docs/apps
access_token = '1725954970975324|sidVOHslF41oAH_KWdlnhNRuDWk' # Put your own access token here! Access tokens are meant to be private for security reasons!It should be a long string of numbers and words

# Look at Bill Gates's profile for this example by using his Facebook id.
user = 'BillGates'

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts')

# Wrap this block in a while loop so we can keep paginating requests until
# finished.
while True:
    try:
        # Perform some action on each post in the collection we receive from
        # Facebook.
        [some_action(post=post) for post in posts['data']]
        # Attempt to make a request to the next page of data, if it exists.
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
        break