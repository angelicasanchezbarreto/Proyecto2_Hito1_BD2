from nltk.stem import SnowballStemmer

class Operators:
    dic=dict()
    def __init__(self,dic):
        self.dic=dic

    def L(self,word):
        stemmer = SnowballStemmer('spanish')
        newWord = stemmer.stem(word.lower())
        ids = []
        if newWord in self.dic:
            ids=self.dic[newWord]
            print("TweetIds for",word,":",ids)
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
