import tweepy
from textblob import TextBlob
import csv
'''
wiki = TextBlob("Man I'm so angry right now.")
print("tags: " + wiki.tags)
print("sentiment: " + wiki.sentiment)
'''

consumer_key = 'Rg351iTo9b9OKfs4jGyoju2lD'
consumer_secret = '5CvLVuMhrtL2pGn05tfwbvOAQw48Bym5ZnMx5K9SztiM98T46S'

access_token = '2832322316-2vha0jt8QMc9UM3pr3lZPgTFOd05yE51TlcQLA0'
access_token_secret = '3z1fFQ546aSKl6IB7CXI9sdRrBv8AEVK63ShcS7F0MPZd'

# this method logs in via code
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#using api we can create, delete, find twitter users, etc
api = tweepy.API(auth)

#we gona collect tweets that contain a certain keyword
public_tweets = api.search('Drake', count=5000)

csv_file = open('tweet_sentiment.csv', encoding='utf-8', mode='w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Tweet', 'Polarity', 'Subjectivity'])

for tweet in public_tweets:
	#print('***********************************')
	#print(tweet.text)
	analysis = TextBlob(ascii(tweet.text.encode('utf-8')))
	#print(analysis.sentiment)
	csv_writer.writerow([tweet.text, analysis.sentiment.polarity, analysis.sentiment.subjectivity])

csv_file.close()

