import os
from parser import Parser
from invertedIndex import InvertedIndex
from functions import Functions
import json

#directory = r"/home/lica-pc/2020-2/Base de Datos/Proyecto2/Hito1/Proyecto2_Hito1_BD2/clean"

#directory = os.path.join(os.getcwd(), os.listdir(os.getcwd())[5]) #para clean
directory = os.path.join(os.getcwd(), os.listdir(os.getcwd())[2]) #para prueba


class Console:
    parser = Parser(directory)
    inverted_index = InvertedIndex(parser.my_tweets)
        
    def print_in_console(self):
        print("Ingresa la palabra a buscar:")
        query = input()
        functions = Functions(self.inverted_index,self.parser.my_tweets)
        query_terms = functions.retrieval_cosine(query)
        #for term in query_terms:
            #self.print_full_tweet(term)
        print(query_terms)
        #print(self.inverted_index.norms)
        
    def print_full_tweet(self,tweet_id):
        for filename in self.parser.my_tweets_docs:
            file = open("prueba/"+filename)
            json_object = json.load(file)
            for tweet in json_object:
                if tweet_id == tweet["id"]:
                    print(tweet,"\n")
        

console = Console()
console.print_in_console()