import tweepy,os

# Authenticate to Twitter
auth = tweepy.OAuthHandler("olQxB5rcfMrviCHWlevoGfIQ0", "KKo5x1iDqwnKemBtdT6Im2yAxSGHYv7VimOOLTsOFn6jzwfndr")
auth.set_access_token("1367941050942230529-Nh2ei0cjXogMzUA2hz33TCeOOJctfx", "jIYkiuhttdaMUiNLLji4ym7sjG5i2CszFOLsTJymLdPfS")

# Create API object
api = tweepy.API(auth)

# Create a tweet
#api.update_status("Hi my name is Jokrr and this is a test from my python bot")

# Send a DM to an account

recipient_id = 1270664136670810112

text = input("Please enter the message you would like to send\n")

direct_message = api.send_direct_message(recipient_id, text)
print(direct_message.message_create['message_data']['text'])
