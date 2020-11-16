import os
from parser import Parser
from invertedIndex import InvertedIndex
from functions import Functions


class Console:
    my_tweets = dict()
    my_tweets_index = dict()
    def __init__(self,my_tweets,my_tweets_index):
        self.my_tweets = my_tweets
        self.my_tweets_index = my_tweets_index
        
    def print_in_console(self):
        print("Ingresa la palabra a buscar:")
        query = input()
        op = Functions(self.my_tweets_index,self.my_tweets)
        query_terms = op.retrieval_cosine(query)
        print(query_terms)


#directory = r"/home/lica-pc/2020-2/Base de Datos/Proyecto2/Hito1/Proyecto2_Hito1_BD2/clean"

#directory = os.path.join(os.getcwd(), os.listdir(os.getcwd())[5]) #para clean
directory = os.path.join(os.getcwd(), os.listdir(os.getcwd())[2]) #para prueba

parser = Parser(directory)
my_tweets_index = InvertedIndex(parser.my_tweets)

#index.print()
#result1 = op.OR(op.L("Legales"),op.L("Cortesia"))

console = Console(parser.my_tweets,my_tweets_index.dic)
console.print_in_console()