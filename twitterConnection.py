import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import socket
import json

consumer_key='qnk947wN9ap5qJlKVohMD1Yjv'
consumer_secret='5qfCgRlEeGNiX0lnA6QLhHSQp1JmQDTPMmh6wXWt6bggcn0j04'
access_token ='1438453799824285696-iRnO6j6vevxFUO0m69PlPm3YL0nzhz'
access_secret='O0MycHCz6k9EqzoZsl6G4mQvxvlswimptok0yt3JSRi52'

class TweetsListener(StreamListener):
    def __init__(self, csocket):
        self.client_socket = csocket
    def on_data(self, data):
        try:  
            msg = json.loads( data )
            print("new message")
            if "extended_tweet" in msg:
                self.client_socket\
                .send(str(msg['extended_tweet']['full_text']+"t_end")\
                      .encode('utf-8'))         
                print(msg['extended_tweet']['full_text'])
            else:
                self.client_socket\
                .send(str(msg['text']+"t_end")\
                      .encode('utf-8'))
                print(msg['text'])
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    def on_error(self, status):
        print(status)
        return True

def sendData(c_socket, keyword):
    print('start sending data from Twitter to socket')
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    twitter_stream = Stream(auth, TweetsListener(c_socket))
    twitter_stream.filter(track = keyword, languages=["en"])

if __name__ == "__main__":
    # server (local machine) creates listening socket
    s = socket.socket()
    port = 1234
    s.bind((socket.gethostname(), port))
    print('socket is ready')
    # server (local machine) listens for connections
    s.listen(10)
    print('socket is listening')
    # return the socket and the address on the other side of the connection (client side)
    c_socket, addr = s.accept()
    print("Received request from: " + str(addr))
    # select here the keyword for the tweet data
    sendData(c_socket, keyword = ['piano'])
         