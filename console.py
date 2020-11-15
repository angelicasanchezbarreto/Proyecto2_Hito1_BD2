import os
from parser import Parser
from invertedIndex import InvertedIndex
from operators import Operators


class Console:
    my_tweets = dict()
    my_tweets_index = dict()
    def __init__(self,my_tweets,my_tweets_index):
        self.my_tweets = my_tweets
        self.my_tweets_index = my_tweets_index
        
    def print_in_console(self):
        print("Ingresa la palabra a buscar:")
        word = input()
        op = Operators(self.my_tweets_index)
        docs = op.L(word)
        for doc in docs:
            print(self.my_tweets[doc[0]])


#directory = r"/home/lica-pc/2020-2/Base de Datos/Proyecto2/Hito1/Proyecto2_Hito1_BD2/clean"

#directory = os.path.join(os.getcwd(), os.listdir(os.getcwd())[5]) #para clean
directory = os.path.join(os.getcwd(), os.listdir(os.getcwd())[2]) #para prueba

parser = Parser(directory)
my_tweets_index = InvertedIndex(parser.my_tweets)

#index.print()
#result1 = op.OR(op.L("Legales"),op.L("Cortesia"))

console = Console(parser.my_tweets,my_tweets_index.dic)
console.print_in_console()