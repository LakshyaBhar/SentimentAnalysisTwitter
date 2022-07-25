#Python Code
import tweepy
5
from textblob import TextBlob
6
​
7
#providing consumer_key and consumer_secret keys
8
consumer_key='iyJwxDNEaD5ZXauR22Zztn3La'
9
consumer_secret ='uX3lOrn0ElWu6bYKA0SFxFp9pC39PNTIOB3l6d0wcb3Zx0uDHY'
10
​
11
#providing access_token and access_token_secret keys
12
access_token = '1392178314425421824-vaoctnh1WR4DnNkQYEVCq0yEUVV4Pl'
13
access_token_secret ='ifl5odhQZLy1sedbAsMYor2y7B4zHwH9nEwKNqOuAztCU'
14
​
15
​
16
pos=0
17
neg=0
18
neu=0
19
​
20
​
21
#try block
22
try:
23
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
24
    auth.set_access_token(access_token,access_token_secret)
25
    api = tweepy.API(auth)
26
    public_tweets = api.search('injustice')
27
    for tweet in public_tweets:
28
        print(tweet.text)
29
        analysis = TextBlob(tweet.text)
30
        print(analysis.sentiment)
31
        if analysis.sentiment.polarity>0:
32
            print("POSITIVE")
33
            pos=pos+1
34
        elif analysis.sentiment.polarity==0:
35
            print("NEUTRAL")
36
            neu=neu+1
37
        else:
38
            print("NEGATIVE")
39
            neg=neg+1
40
​
41
#except block
42
except:
43
    print("Error:Authentication Failed")
44
​
