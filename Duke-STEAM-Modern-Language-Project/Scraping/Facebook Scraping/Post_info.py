'''
Created on Mar 8, 2016
Scrapes Facebook posts for text content
@author: lucy
'''
import facebook
import requests

def getPost(post):
    print(post['message'])

access_token = '1725954970975324|sidVOHslF41oAH_KWdlnhNRuDWk'
#user = 'The New York Times'

graph = facebook.GraphAPI(access_token)
#profile = graph.get_object(user)
#posts = graph.get_connections(profile['id'], 'posts')
post=graph.get_object(id='nytimes_10150767289159999')
print(post['message'])

'''
while True:
    try:
        # Perform some action on each post in the collection we receive from
        # Facebook.
        [getPost(post=post) for post in posts['data']]
        # Attempt to make a request to the next page of data, if it exists.
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        # When there are no more pages (['paging']['next']), break from the
        # loop and end the script.
        break
    '''