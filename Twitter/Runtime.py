from tweepy.streaming import StreamListener


class Listener(StreamListener):
    '''
        A basic Listener for the Tweepy package.
        All this does is handle listening in a multithreaded environment and pushes data back to our already
        instantiated "responder (r)" class.
    '''

    def __init__(self, r):
        self.r = r

    def on_data(self, data):
        self.r.add_tweet(data)

    def on_error(self, status):
        print "Error: " + status
        return True
