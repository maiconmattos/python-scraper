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

print(api)

teamA = '@Galway_GAA'
teamB = '@MayoGAA'

for status in tweepy.Cursor(api.user_timeline, screen_name="officialgaa", count=5000).items(500):
	text = status.text.encode('ascii','ignore')
	
	if (  (text.startswith('LATEST') or text.startswith('FULL-TIME') or text.startswith('HALF-TIME') ) 
	    and text.find("SFC")>=0 and text.find(teamA)>=0 and text.find(teamB)>=0) :
	    print(text)
	    print("")