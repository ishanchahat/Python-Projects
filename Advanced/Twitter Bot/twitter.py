import tweepy

api_key = "WgyA4GLLVLvqO9kAgkXl3yWwp"
api_secret = "TNtxfC00bfLMI3BscF5zMOooVEYJjdnrGjTLaqcP2TyPqjCHQE"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAEN6ugEAAAAAEC0WSOz0O0s9MF%2BHXX%2BsMRGYKQU%3DDIzV2mRct4bIfnjkQMtd5s1FW0bOhoNMyfmqNRnATdieVfJHTh"
access_token = "1806637612746285056-AJPOpoociQjPpNpRNolWbmy6HdlOKQ"
access_token_secret = "CA2oISdeF3XMQ21DUsBnIYwmsels62U2WEMvruJyJE0bU"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


client.create_tweet(text = "Hello Twitter")

# client.like("1809490840806695352")