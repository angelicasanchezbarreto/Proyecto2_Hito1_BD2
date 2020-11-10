import os
import json
from invertedIndex import InvertedIndex
from operators import Operators

#directory = r"/home/lica-pc/2020-2/Base de Datos/Proyecto2/Hito1/Proyecto2_Hito1_BD2/clean"

#directory = os.path.join(os.getcwd(), os.listdir(os.getcwd())[5]) #para clean
directory = os.path.join(os.getcwd(), os.listdir(os.getcwd())[2]) #para prueba
#print(directory)


my_tweets_docs = []
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        my_tweets_docs.append(filename)
    else:
        continue
my_tweets_docs.sort()

my_tweets = dict()
for filename in my_tweets_docs:
    #file = open("clean/"+filename)
    file = open("prueba/"+filename)
    json_object = json.load(file)
    for tweet in json_object:
        id = tweet["id"]
        text = tweet["text"]
        my_tweets[id]=text

index = InvertedIndex(my_tweets)
#index.print()


op = Operators(index.dic)

result1 = op.OR(op.L("Legales"),op.L("Cortesia"))
