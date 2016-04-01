import tweepy
from tweepy import OAuthHandler
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy
import mmap

negative_words_file=open('negative-words.txt')
negative_words = mmap.mmap(negative_words_file.fileno(), 0, access=mmap.ACCESS_READ)
positive_words_file=open('positive-words.txt')
positive_wordss = mmap.mmap(positive_words_file.fileno(), 0, access=mmap.ACCESS_READ)
consumer_key = 'APe74j0gQL47Qsp0xHSmxGsqQ'
consumer_secret = 'SlRZIDYEbSPIHO28qwFS2rKCwdQgnkiImHvsEzCvFjdBmtQfL1'
access_token = '269631612-nOz98VEBW8WWCLiVVvPd5EHBzXwJdXHzNNGHuHQi'
access_secret = 'TjwifaCX8jI2RRcdD0zmmYrYfQx9sOREld98ezAeEv0TK'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

list_tweets = []
list_tweets_emotion = []
for mytweets in tweepy.Cursor(api.search, q='#TerrorismHasNoReligion', lang='en').items(2):
	tweet_data = unicode(mytweets.text).encode('utf-8')
	list_tweets.append(tweet_data)
	temp_emotion_tweet = []
	for word in tweet_data.split():
		# if word in negative_words or word in positive_words:
		if negative_words.find(word) != '-1' or positive_words.find(word) != '-1':
			temp_emotion_tweet.append(word)
	list_tweets_emotion.append(' '.join(temp_emotion_tweet))


# print list_tweets

tfidf_vectorizer = TfidfVectorizer()

tfidf_matrix_abstraction = tfidf_vectorizer.fit_transform(list_tweets)
matrix_cosine_abstraction = cosine_similarity(tfidf_matrix_abstraction, tfidf_matrix_abstraction)


tfidf_matrix_emotion = tfidf_vectorizer.fit_transform(list_tweets_emotion)
matrix_cosine_emotion = cosine_similarity(tfidf_matrix_emotion, tfidf_matrix_emotion)

# print tfidf_matrix_abstraction
# print tfidf_matrix_emotion
