import tweepy
from tweepy import OAuthHandler
import json
 
consumer_key = 'N3bIWe0YODH0tiN1mBOvn1xU3'
consumer_secret = '3wKjm8FFZBY4JtJzyAaHkYcCdGLiOYPgGIFhiANLSVGp1lvf2b'
access_token = '874639429268381696-DkspeBInwdr3m1Bh5SsQnIbD1rAzVuh'
access_secret = 'tkYZUbFKzFVHUOQBj2sYWsUZMFrfDdTx40SEBMwSUipAE'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
print("Connected on twitter :" + str(api))

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
    	text = status.text
    	if (text.find("SFC")>=0):
            if (text.startswith('LATEST')):
            	parseLatest(status.text)
            elif (text.startswith('HALF-TIME') or text.startswith('HALF TIME') or text.startswith('HALFTIME')): 
                parseHalfTime(status.text)
            elif (text.startswith('FULL-TIME') or text.startswith('FULL TIME') or text.startswith('FULLTIME')): 
	            parseFullTime(status.text)

def parseLatest(text):
    print("LATEST ====> " + text)

def parseHalfTime(text):
    print("HALF-TIME ====> " + text)

def parseFullTime(text):
    print("FULL-TIME ====> " + text)            

myStreamListener = MyStreamListener
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener())

myStream.filter(follow=['874639429268381696'])
#843856454 - @mobstatsmob
#89700550 - @officialgaa
#874639429268381696 - @maiconmattos83


