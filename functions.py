import nltk
from nltk.stem import SnowballStemmer
from tokens import Tokens
import collections
import math 
from invertedIndexMem import InvertedIndexMem
from invertedIndex import tf
import numpy as np
import operator

class Functions:
    inverted_index = InvertedIndexMem()
    
    def __init__(self,inverted_index):
        self.inverted_index=inverted_index

    def L(self,word):
        stemmer = SnowballStemmer('spanish')
        newWord = stemmer.stem(word.lower())
        ids = self.inverted_index.get_doc_ids(newWord)
        if len(ids)>0:
            print("TweetIds for",word,":",ids,"\n")
        else:
            print("The word",word,"does not belong to the documents.")
        return ids
        
            
    def AND(self,list1,list2):
        answer=[]
        if len(list1) > len(list2):
            for i,freq in list1:
                if i in list2:
                    answer.append((i,freq))
        else:
            for i,freq in list2:
                if i in list1:
                    answer.append((i,freq))
        print("AND result:",answer)
        return answer

    def OR(self,list1,list2):
        answer=[]
        if len(list1) > len(list2):
            answer = list1
            for i,freq in list2:
                if i not in answer:
                    answer.append((i,freq))
        else:
            answer = list2
            for i,freq in list1:
                if (i,freq) not in answer:
                    answer.append((i,freq))
        print("OR result:",answer)
        return answer

    def NOT(self,list1,list2):
        answer=[]
        answer = list1.copy()
        for i,freq in list1:
            if (i,freq) in list2:
                answer.remove((i,freq))
        print("NOT result:",answer)
        return answer
    
    def get_query_norms(self,query_weights):
        data = list(query_weights.values())
        norma = round(np.linalg.norm(data),2)
        return norma
    
    def retrieval_cosine(self,query):
        scores = dict()
        tokens = Tokens()
        query_terms = tokens.edit_query(query)
        query_weights = dict(collections.Counter(query_terms).items())
        for query in query_weights:
            query_weights[query] = tf(query_weights[query])
        
        for query in query_weights:
            term = query
            doc_ids = self.L(term)
            for doc in doc_ids:
                if doc[0] not in scores:
                    scores[doc[0]] = tf(doc[1])*tf(query_weights[term])
                else:
                    new_value = scores[doc[0]] + tf(doc[1])*tf(query_weights[term])
                    scores[doc[0]] = new_value
        for id in scores:
            norm_value = self.inverted_index.get_norms(str(id))
            scores[id] = round(scores[id]/(norm_value*self.get_query_norms(query_weights)),2)
        scores = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
        return scores