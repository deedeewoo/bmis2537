try:
	tso = TwitterSearchOrder()#create a TwitterSearchOrder Object
	tso.set_keywords(['Fuji', 'Xerox'])#specify keywords
	tso.set_geocode(36.778261, -119.417932,200,imperial_metric=True)
	tso.set_language('en')#language of tweets
	tso.set_include_entities(False)
	ts = TwitterSearch(
     	consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
     	consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
     	access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
     	access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    	)
	for tweet in ts.search_tweets_iterable(tso):
		print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
except TwitterSearchException as e:
	print(e)
