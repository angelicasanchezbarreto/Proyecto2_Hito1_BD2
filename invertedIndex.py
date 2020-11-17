from tokens import Tokens
import pandas as pd
import numpy as np
import json
import math 

def tf(num):
    return round(math.log10(1+num),2)

def idf(num,N):
    return round(math.log10(N/num),2)

class InvertedIndex:
    dic=dict()
    my_tweets_dic=dict()
    tf_idf_dic=dict()
    norms_dic=dict()
    norms=dict()
    def __init__(self,my_tweets_dic):
        self.my_tweets_dic=my_tweets_dic
        self.execute_index()

    def execute_index(self):
        self.dic = self.set_index_dic(self)
        self.set_tf_idf()
        self.write_files()
        return self.dic
    
    def write_files(self):
        self.write_index_to_file()
        self.write_size_to_file()
        self.write_tfidf_to_file()
        self.write_norms_to_file()

    def replace_in_dic(self,word,current_id):
        if (word in self.dic):
            ids = self.dic[word]
            already_in=False
            for i,freq in ids:
                if current_id is i: 
                    already_in=True
                    new_pair = (current_id,freq+1)
                    new_list = [new_pair if current_id in item else item for item in ids]
                    self.dic[word]=new_list
            if already_in is False:
                self.dic[word].append((current_id,1))
        else:
            self.dic.setdefault(word,[]).append((current_id,1))
    
    def set_index_dic(self,my_tweets_dic):
        for tweet_id in self.my_tweets_dic:
            tokens = Tokens()
            tokens.remove_stopwords(self.my_tweets_dic[tweet_id])
            current_id = tweet_id
            for word in tokens.reduced_tokens:
                self.replace_in_dic(word,current_id)
                
        sorted_dic = dict(sorted(self.dic.items()))
        return sorted_dic
    
    def set_tf_idf(self):
        N = len(self.my_tweets_dic)
        for term in self.dic:
            docs = self.dic[term] #doc list of pairs
            size = len(docs)
            for doc_freq in docs:
                tf_idf = round(tf(doc_freq[1])*idf(size,N),2)
                self.tf_idf_dic.setdefault(doc_freq[0],[]).append((term,tf_idf))
                self.norms_dic.setdefault(doc_freq[0],[]).append(tf_idf)
        self.set_norms()
        
    def set_norms(self):
        for id in self.norms_dic:
            self.norms[id] = round(np.linalg.norm(self.norms_dic[id]),2)
        
    def print_inverted_index(self):
        for item in self.dic:
            print(item,self.dic[item])

    def write_index_to_file(self):
        with open('files/indexFile.json','w') as file:
            json.dump(self.dic,file)

    def write_tfidf_to_file(self):
        with open('files/tfidf.json','w') as file:
            json.dump(self.tf_idf_dic,file)
    
    def write_norms_to_file(self):
        with open('files/norms.json','w') as file:
            json.dump(self.norms,file)
            
    def write_size_to_file(self):
        n_size = len(self.my_tweets_dic)
        with open('files/size.txt','w') as file:
            json.dump(n_size,file)