import tweepy,os

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMERKEY", "CONSUMER_SECRET") # Auth with the keys you get through twitter dev portal
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

# Send a DM to specified account

recipient_id = input("Please enter the numeric ID of the twitter user you would like to DM\n")

text = input("Please enter the message you would like to send\n")

direct_message = api.send_direct_message(recipient_id, text)
print(direct_message.message_create['message_data']['text'])
