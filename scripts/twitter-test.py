import os
import twitter 
from TwitterSearch import *

### IN THE FOLLOWING CODE, PLEASE REPLACE CONSUMER KEY, 
### CONSUMER SECRET, ACCESS TOKEN AND 
### ACCESS TOKEN SECRET WITH THE VALUES FROM PREVIOUS SECTION. 

try:
	tso = TwitterSearchOrder()  #create a TwitterSearchOrder Object
	tso.set_keywords(['TensorFlow'])  #specify keywords
	tso.set_geocode(37.7749295, -122.4194155, 500, imperial_metric=True)   
	#setGeocode(latitude<float>,longitude<float>, radius<int,long>, imperial_metric <True/False>)
	tso.set_language('en')#language of tweets
	tso.set_include_entities(False)
	#create a TwitterSearch object using your API keys and tokens
	ts = TwitterSearch(consumer_key = 'S6C74cnpFTYCg63tQU1IrumLr', 
	consumer_secret = 'KIp5xpMxZXzSP68ipaks40Tg479bFkf1N0cfDGAuIQbol67mOU', 
	access_token = '66107280-wj4j8usIjRBXXRqRPMLD5I8u5CZJ4x8hajSUILK2o', 
	access_token_secret = 'swpIQc7wTANBB3CCgo42syhVc6GBnv3aqjfqebp3C7Rdn')
	for tweet in ts.search_tweets_iterable(tso):
		print('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text']))
except TwitterSearchException as e:
	print(e)