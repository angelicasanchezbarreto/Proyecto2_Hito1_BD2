import os
from parser import Parser
from invertedIndex import InvertedIndex
from functions import Functions
import json

class Console:
    my_tweets = dict()
    inverted_index = dict()
    tf_idf_dic = dict()
    my_tweets_docs = []
    def __init__(self,my_tweets,my_tweets_docs,inverted_index,tf_idf_dic):
        self.my_tweets = my_tweets
        self.my_tweets_docs = my_tweets_docs
        self.inverted_index = inverted_index
        self.tf_idf_dic = tf_idf_dic
        
    def print_in_console(self):
        print("Ingresa la palabra a buscar:")
        query = input()
        op = Functions(self.inverted_index,self.my_tweets,self.tf_idf_dic)
        query_terms = op.retrieval_cosine(query)
        for term in query_terms:
            self.print_full_tweet(term)
        print(query_terms)
        
    def print_full_tweet(self,tweet_id):
        for filename in self.my_tweets_docs:
            file = open("prueba/"+filename)
            json_object = json.load(file)
            for tweet in json_object:
                if tweet_id == tweet["id"]:
                    print(tweet,"\n")
        

#directory = r"/home/lica-pc/2020-2/Base de Datos/Proyecto2/Hito1/Proyecto2_Hito1_BD2/clean"

#directory = os.path.join(os.getcwd(), os.listdir(os.getcwd())[5]) #para clean
directory = os.path.join(os.getcwd(), os.listdir(os.getcwd())[2]) #para prueba

parser = Parser(directory)
inverted_index = InvertedIndex(parser.my_tweets)
console = Console(parser.my_tweets,parser.my_tweets_docs,inverted_index.dic,inverted_index.tf_idf_dic)
console.print_in_console()