import tweepy
from tweepy import OAuthHandler
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy
import mmap
from nltk.corpus import stopwords

try:
	negative_words = [line.strip() for line in open("negative-words.txt", 'r')]
	positive_words = [line.strip() for line in open("positive-words.txt", 'r')]

	# consumer_key = 'APe74j0gQL47Qsp0xHSmxGsqQ'
	# consumer_secret = 'SlRZIDYEbSPIHO28qwFS2rKCwdQgnkiImHvsEzCvFjdBmtQfL1'
	# access_token = '269631612-nOz98VEBW8WWCLiVVvPd5EHBzXwJdXHzNNGHuHQi'
	# access_secret = 'TjwifaCX8jI2RRcdD0zmmYrYfQx9sOREld98ezAeEv0TK'
	 
	# auth = OAuthHandler(consumer_key, consumer_secret)
	# auth.set_access_token(access_token, access_secret)
	 
	# api = tweepy.API(auth)

	original_tweets = open("tweets.txt", 'r')

	list_tweets_abstraction = []
	list_tweets_emotion = []
	list_tweets = []
	stopwords = stopwords.words('english')
	for i,term in enumerate(stopwords):
		stopwords[i] = term.encode('utf-8')


	# for mytweets in tweepy.Cursor(api.search, q='#TerrorismHasNoReligion', lang='en').items(5):
	for mytweets in original_tweets:
		# tweet_data = unicode(mytweets.text).encode('utf-8')
		tweet_data = mytweets.lower()
		list_tweets.append(tweet_data)
		tweet_data = tweet_data.replace('#TerrorismHasNoReligion'.lower(),'')
		temp_emotion_tweet = []
		temp_abstract_tweet = []
		splitted_tweet = tweet_data.split()
		for word in splitted_tweet:
			# if word in negative_words or word in positive_words:
			if word in negative_words != -1 or word in positive_words != -1:
				temp_emotion_tweet.append(word)
			else:
				if word not in stopwords and len(word) >= 2:
					temp_abstract_tweet.append(word)
		list_tweets_abstraction.append(' '.join(temp_abstract_tweet))
		list_tweets_emotion.append(' '.join(temp_emotion_tweet))

	print "---------list tweets-------------"
	print list_tweets_abstraction

	print "---------list emotion tweets--------------"
	print list_tweets_emotion
	tfidf_vectorizer = TfidfVectorizer()

	tfidf_matrix_abstraction = tfidf_vectorizer.fit_transform(list_tweets_abstraction)
	matrix_cosine_abstraction = cosine_similarity(tfidf_matrix_abstraction, tfidf_matrix_abstraction)
	numpy.savetxt("cosine_abstraction.csv", matrix_cosine_abstraction, delimiter=",")

	tfidf_matrix_emotion = tfidf_vectorizer.fit_transform(list_tweets_emotion)
	matrix_cosine_emotion = cosine_similarity(tfidf_matrix_emotion, tfidf_matrix_emotion)
	numpy.savetxt("cosine_emotion.csv", matrix_cosine_emotion, delimiter=",")

	list_tweets_file = open('list_tweets', 'w')
	list_tweets_file.write("\n".join(list_tweets))
	print "---------matrix_cosine_emotion---------------"
	print matrix_cosine_emotion

	print "---------matrix_cosine_abstraction---------------"
	print matrix_cosine_abstraction
except IOError:
	print "some error"
