#Code for sentiment analysis of tweets to understand major issues of products/companies
#Lakshya Bhardwaj

import tweepy
from textblob import TextBlob

#providing consumer_key and consumer_secret keys
consumer_key='iyJwxDNEaD5ZXauR22Zztn3La'
consumer_secret ='uX3lOrn0ElWu6bYKA0SFxFp9pC39PNTIOB3l6d0wcb3Zx0uDHY'

#providing access_token and access_token_secret keys
access_token = '1392178314425421824-vaoctnh1WR4DnNkQYEVCq0yEUVV4Pl'
access_token_secret ='ifl5odhQZLy1sedbAsMYor2y7B4zHwH9nEwKNqOuAztCU'


pos=0
neg=0
neu=0


#try block
try:
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    public_tweets = api.search('injustice')
    for tweet in public_tweets:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
        if analysis.sentiment.polarity>0:
            print("POSITIVE")
            pos=pos+1
        elif analysis.sentiment.polarity==0:
            print("NEUTRAL")
            neu=neu+1
        else:
            print("NEGATIVE")
            neg=neg+1

#except block
except:
    print("Error:Authentication Failed")
