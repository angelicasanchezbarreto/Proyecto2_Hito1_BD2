import os
from parser import Parser
from invertedIndex import InvertedIndex
from functions import Functions


class Console:
    my_tweets = dict()
    inverted_index = dict()
    tf_idf_dic = dict()
    def __init__(self,my_tweets,inverted_index,tf_idf_dic):
        self.my_tweets = my_tweets
        self.inverted_index = inverted_index
        self.tf_idf_dic = tf_idf_dic
        
    def print_in_console(self):
        print("Ingresa la palabra a buscar:")
        query = input()
        op = Functions(self.inverted_index,self.my_tweets,self.tf_idf_dic)
        query_terms = op.retrieval_cosine(query)
        print(query_terms)


#directory = r"/home/lica-pc/2020-2/Base de Datos/Proyecto2/Hito1/Proyecto2_Hito1_BD2/clean"

#directory = os.path.join(os.getcwd(), os.listdir(os.getcwd())[5]) #para clean
directory = os.path.join(os.getcwd(), os.listdir(os.getcwd())[2]) #para prueba

parser = Parser(directory)
inverted_index = InvertedIndex(parser.my_tweets)
console = Console(parser.my_tweets,inverted_index.dic,inverted_index.tf_idf_dic)
console.print_in_console()