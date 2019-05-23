import tweepy
 
# Consumer keys and access tokens, used for OAuth
consumer_key = 'ivXoCzbsproSiZxXjclnxB2Ix'
consumer_secret = 't8NNlTvlWZ8KxzCALVKh1e1P8LCDAO0eRl6bPyiULoofQ9TqNc'
access_token = '1131114814770745344-ypIJJd5aYzZSjf8bxdy3f26TLEWclO'
access_token_secret = 'vP3Oh8UWildlAQGWSMOn30lBvmbGZQ3foDkugXEaBY6Ll '
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 
# Sample method, used to update a status
api.update_status('Hello Python Central!')