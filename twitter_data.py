import tweepy
from tweepy import OAuthHandler
from nltk.tokenize import word_tokenize
 
consumer_key = 'APe74j0gQL47Qsp0xHSmxGsqQ'
consumer_secret = 'SlRZIDYEbSPIHO28qwFS2rKCwdQgnkiImHvsEzCvFjdBmtQfL1'
access_token = '269631612-nOz98VEBW8WWCLiVVvPd5EHBzXwJdXHzNNGHuHQi'
access_secret = 'TjwifaCX8jI2RRcdD0zmmYrYfQx9sOREld98ezAeEv0TK'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

for mytweets in tweepy.Cursor(api.search, q='#TerrorismHasNoReligion', lang='en').items(100):
	print unicode(mytweets.text).encode('utf-8')