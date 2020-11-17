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
    df_dic=pd.DataFrame
    tf_idf_dic=dict()
    norms_dic=dict()
    norms=dict()
    def __init__(self,my_tweets_dic):
        self.my_tweets_dic=my_tweets_dic
        self.execute_index()

    def execute_index(self):
        self.dic = self.set_index_dic(self)
        self.set_tf_idf()
        self.write_to_file()
        return self.dic
    
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
        #df_dic = self.get_data_frame()
        #print(sorted_dic)
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
        #print(self.tf_idf_dic,"\n")
        #print(vector)
        
    def set_norms(self):
        for id in self.norms_dic:
            self.norms[id] = round(np.linalg.norm(self.norms_dic[id]),2)
    
    def get_data_frame(self):
        self.df_dic = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in self.dic.items() ])).T.rename_axis('Term').add_prefix('tweetIds')
        self.df_dic.sort_values(by=['Term'], inplace=True)
        self.df_dic.reset_index(inplace=True)
        return self.df_dic
        
    def print_full_dataframe(self):
        self.get_data_frame()
        pd.set_option('display.max_rows', len(self.df_dic))
        print(self.df_dic)
        pd.reset_option('display.max_rows')
        
    def print_inverted_index(self):
        for item in self.dic:
            print(item,self.dic[item])

    def write_to_file(self):
        with open('indexFile.txt','w') as file:
            file.write(json.dumps(self.dic))