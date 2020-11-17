import os
from parser import Parser
from invertedIndex import InvertedIndex
from invertedIndexMem import InvertedIndexMem
from functions import Functions
import json

#directory = os.path.join(os.getcwd(), os.listdir(os.getcwd())[5]) #para clean
directory = os.path.join(os.getcwd(), os.listdir(os.getcwd())[3]) #para prueba
print(directory)

class Console:
    #parser = Parser(directory)
    #inverted_index = InvertedIndex(parser.my_tweets)
    n_size = 0
    inverted_index_mem = InvertedIndexMem()
    
    def get_size(self):
        with open('size.txt','r') as file:
            self.n_size = file
     
    def print_in_console(self):
        print("Ingresa la palabra a buscar:")
        query = input()
        functions = Functions(self.inverted_index_mem)
        query_terms = functions.retrieval_cosine(query)
        #for term in query_terms:
            #self.print_full_tweet(term)
        print(query_terms)
        #print(self.inverted_index.norms)
        
    def print_full_tweet(self,tweet_id):
        tweet = self.inverted_index_mem.get_tweet(tweet_id)
        print(tweet,"\n")
        

console = Console()
console.print_in_console()
    