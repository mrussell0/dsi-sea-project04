#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import csv
import json

#Variables that contains the user credentials to access Twitter API
consumer_key = 'agWI6gK7yNeTPbuC3M3MnNiQ9'
consumer_secret = 'wx9Q5a8KvBxh4usMqLylRqQfmM1kl7gDV0mrRaDbCjCh3zbmoz'
access_token = '55475956-pvQdaNi9T3W92VRzBa82U6RtF2cn7ydVLqE51clSO'
access_token_secret = 'zSO3XK4ob0bMKLH3JOkZsca6yvDC8NqLZVUY8iJ5prcna'

start_time = time.time()

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def __init__(self, start_time, time_limit=10):

        self.time = start_time
        self.limit = time_limit

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l, StdOutListener(start_time, time_limit=20))

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['trump', 'clinton', 'hillary', 'donald'])
