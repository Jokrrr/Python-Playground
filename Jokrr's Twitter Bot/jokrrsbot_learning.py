import tweepy,os

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMERKEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

# Create a tweet
#api.update_status("Hi my name is Jokrr and this is a test from my python bot")

# Send a DM to an account

recipient_id = 1270664136670810112

text = input("Please enter the message you would like to send\n")

direct_message = api.send_direct_message(recipient_id, text)
print(direct_message.message_create['message_data']['text'])
