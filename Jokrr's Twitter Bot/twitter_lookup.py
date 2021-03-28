import tweepy,os

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMERKEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)
