import tweepy
from textblob import TextBlob
import re

polarity = 0
numberoftweets = 0
average = 0
numneg = 0
numpos = 0
numneu = 0

auth = tweepy.OAuthHandler('eoWSW9nGuDnuetWn5DuRbV1Xp', 'JuaBKJa0oYuZFzQe3cv4Ajuq4d7wfoD9RboBeF3otA28UOgbGj')
auth.set_access_token('1053705516357083136-czN4zFt29SXJxgwgzQiLXpnCnYGpjS', 'poYFeGPqAzTr7yF47geTVecSN6dYH1aeOuXdONEr8CeDk')

api = tweepy.API(auth)

x = input("Enter a Topic: ")
print("\n")

public_tweets = api.search(x)

def clean_tweet(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def determine_polarity(tweet):
    if polarity >= -.25 and polarity <= .25:
        numneu += 1
        
    if polarity < -.25:
        numneg += 1
        
    if polarity > .25:
        numpos += 1
        
                               
for tweet in public_tweets:
    print(clean_tweet(str(tweet.text)))
    numberoftweets += 1
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    polarity = analysis.sentiment.polarity
    if polarity >= -.05 and polarity <= .05:
        numneu += 1
    if polarity < -.05:
        numneg += 1
    if polarity > .05:
        numpos += 1
    print("\n")

    
            
average = polarity/numberoftweets

print("Percent Positive: " + str((numpos/numberoftweets)*100)+"%")

print("Percent Neutral: " + str((numneu/numberoftweets)*100)+"%")

print("Percent Negative: " + str((numneg/numberoftweets)*100)+"%")
