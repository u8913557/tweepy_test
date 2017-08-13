# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 11:40:33 2017

@author: alter
"""


import tweepy
#from twython import Twython

consumer_key='xqGA9sL9Nu3TfqVMAc7igcOmh'
consumer_secret='zMgP9dCP29FPc1ko2DTxyBtqI9YIFFUoHOWmFaTlxGvkaoHBbL'
access_token='24269777-JfwWaeBGtoRXxXiY1ahXCWr2MCuBijn5aWgEYorib'
access_token_secret='O7kvQeYAW7oG3hVySsWVeVTBPfXCcbLIec1TfPS3DKiIB'

#===========

#twitter = Twython(consumer_key, consumer_secret)
#auth = twitter.get_authentication_tokens(callback_url='http://mysite.com/callback')

#twitter = Twython(consumer_key, consumer_secret, access_token, access_token_secret)
#twitter.update_status(status='See how easy using Twython is!輸入更新的訊息!')
#print(twitter.search(q='FF14'))
#timeline = twitter.get_home_timeline(screenname='u8913557',count=50)
#print(timeline)

#=================

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

public_tweets = api.home_timeline(count = 3)

i = 1
for tweet in public_tweets:
    print('#' +  str(i) + ': ' + tweet.text)
    i = i + 1

api.update_status('Test')
    