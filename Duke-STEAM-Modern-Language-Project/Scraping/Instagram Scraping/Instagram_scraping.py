'''
Created on Mar 17, 2016
Scraping Instagram comments
@author: lucy
'''

import bs4
import requests


def getComments(url):
    res=requests.get(url)
    res.raise_for_status
    print res.text
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    for i in soup.findAll('li',{"class" : "_nk46a"}):
        print i
        #print 'hi'
        #url=i.a['href']
        #print url
        # write all of the urls to a text file
        #herCampusUrls.write(url+'\n')
 
getComments('https://www.instagram.com/p/BDEPypqL2z7/?taken-by=nytimes')
    #driver.quit()