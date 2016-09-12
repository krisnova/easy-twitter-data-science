import json
import time
import datetime

class Tweets(object):
    '''
    This class represents a list of tweets. Here is where we should handle all interaction with the master
    list of tweets. As a convention, if we are interacting with an in-memory list of tweets all sCRUD operations
    should pass through a class method here.
    '''

    List = {}
    TotalTweets = 0

    def add_tweet(self, tweet_json):
        # Todo we need memory checks - this could cause problems blindly filling up the buffer
        self.TotalTweets += 1
        tweet = json.loads(tweet_json)
        # Index our tweets by time
        self.List[tweet['created_at']] = tweet

    def get_tweet(self):
        while len(self.List) < 1:
            pass
        return self.List[self.List.keys()[-1]]

    def get_list_length(self):
        return len(self.List)

    def get_list(self):
        while len(self.List) < 1:
            pass
        l = self.List
        self.List = {}
        return l
