import tweepy
import re
from textblob import TextBlob

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
from forms import RegisterForm



polarity = 0
numberoftweets = 0
average = 0
numneg = 0
numpos = 0
numneu = 0



auth = tweepy.OAuthHandler('eoWSW9nGuDnuetWn5DuRbV1Xp', 'JuaBKJa0oYuZFzQe3cv4Ajuq4d7wfoD9RboBeF3otA28UOgbGj')
auth.set_access_token('1053705516357083136-czN4zFt29SXJxgwgzQiLXpnCnYGpjS', 'poYFeGPqAzTr7yF47geTVecSN6dYH1aeOuXdONEr8CeDk')

api = tweepy.API(auth)


def clean_tweet(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())




app.config['SECRET_KEY'] = '6f02d5173436b1edc582df2986792fd2'

@app.route("/")
@app.route("/home")
@app.route("/sentwiment")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/data")
def data():
    sampledict = {}
    query = request.args.get('query', ' ')
    public_tweets = api.search(q = query, count = 100)
    for tweet in public_tweets:
        cleaned_tweet = clean_tweet(tweet.text)
        analysis = TextBlob(cleaned_tweet)
        polarity = analysis.sentiment.polarity
        sampledict.update({clean_tweet(tweet.text):polarity})
    return jsonify(sampledict)
    

if __name__ == '__main__':
    app.run(debug=True)
