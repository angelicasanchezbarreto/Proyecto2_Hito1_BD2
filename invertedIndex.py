from tokens import Tokens
import pandas as pd
import numpy as np
import json

class InvertedIndex:
    dic=dict()
    my_tweets=dict()
    df_dic=pd.DataFrame
    def __init__(self,my_tweets):
        self.my_tweets=my_tweets
        self.execute_index()

    def execute_index(self):
        self.dic = self.set_index_dic(self)
        self.write_to_file()
        return self.dic
    
    """ def replace_in_dic(self,word,current_id):
        if (word in self.dic):
            ids = self.dic[word]
            already_in=False
            for i in ids:
                if current_id is i: 
                    already_in=True
            if already_in is False:
                self.dic[word].append(current_id)
        else:
            self.dic[word]=[current_id] """
    
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
                #self.dic[word].append(current_id)
        else:
            #self.dic[word]={current_id,1}
            self.dic.setdefault(word,[]).append((current_id,1))
    
    def set_index_dic(self,my_tweets):
        for tweet_id in self.my_tweets:
            tokens = Tokens(self.my_tweets[tweet_id])
            current_id = tweet_id
            for word in tokens.reduced_tokens:
                self.replace_in_dic(word,current_id)
                
        sorted_dic = dict(sorted(self.dic.items()))
        #df_dic = self.get_data_frame()
        #print(sorted_dic)
        return sorted_dic
    
    def get_data_frame(self):
        self.df_dic = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in self.dic.items() ])).T.rename_axis('Term').add_prefix('tweetIds')
        self.df_dic.sort_values(by=['Term'], inplace=True)
        self.df_dic.reset_index(inplace=True)
        return self.df_dic
        
    def print_full(self):
        self.get_data_frame()
        pd.set_option('display.max_rows', len(self.df_dic))
        print(self.df_dic)
        pd.reset_option('display.max_rows')
        
    def print(self):
        for item in self.dic:
            print(item,self.dic[item])

    def write_to_file(self):
        with open('indexFile.txt','w') as file:
            file.write(json.dumps(self.dic))