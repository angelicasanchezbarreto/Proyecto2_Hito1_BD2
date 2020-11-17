import os
import json
import os.path
from multiprocessing import Pool
import sys
import time

class Parser:
    my_tweets_docs = []
    my_tweets = dict()
    
    def __init__(self,directory):
        self.get_tweets(directory)
        self.fill_dic_tweets()
    
    def get_tweets(self,directory):
        for filename in os.listdir(directory):
            if filename.endswith(".json"):
                self.my_tweets_docs.append(filename)
            else:
                continue
        self.my_tweets_docs.sort()

    def fill_dic_tweets(self):
        for filename in self.my_tweets_docs:
            #file = open("clean/"+filename)
            file = open("prueba/"+filename)
            json_object = json.load(file)
            for tweet in json_object:
                id = tweet["id"]
                text = tweet["text"]
                self.my_tweets[id]=text