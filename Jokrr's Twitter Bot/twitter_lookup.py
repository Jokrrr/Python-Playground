import tweepy,os

# Authenticate to Twitter
auth = tweepy.OAuthHandler("olQxB5rcfMrviCHWlevoGfIQ0", "KKo5x1iDqwnKemBtdT6Im2yAxSGHYv7VimOOLTsOFn6jzwfndr")
auth.set_access_token("1367941050942230529-Nh2ei0cjXogMzUA2hz33TCeOOJctfx", "jIYkiuhttdaMUiNLLji4ym7sjG5i2CszFOLsTJymLdPfS")

# Create API object
api = tweepy.API(auth)