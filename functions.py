import nltk
from nltk.stem import SnowballStemmer
from tokens import Tokens
import collections
import math 
import numpy as np

def tf(num):
    return round(math.log10(1+num),2)

def idf(num,N):
    return round(math.log10(N/num),2)

class Functions:
    my_tweets = dict()
    inverted_index = dict()
    tf_idf_dic = dict()
    def __init__(self,inverted_index,my_tweets,tf_idf_dic):
        self.inverted_index=inverted_index
        self.my_tweets=my_tweets
        self.tf_idf_dic=tf_idf_dic

    def L(self,word):
        stemmer = SnowballStemmer('spanish')
        newWord = stemmer.stem(word.lower())
        ids = []
        if newWord in self.inverted_index:
            ids=self.inverted_index[newWord]
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
    
    #def get_norms(self,dictionary):
        

        #normas = np.linalg.norm(vector)
        #for elem,i in dictionary:
         #   new_dic[elem] = normas[i]
    
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
        """ norms = self.get_norms(self.inverted_index)
        for id in scores:
            scores[id] = scores[id]/(norms[id]*self.get_norms(query_terms)) """
        return scores