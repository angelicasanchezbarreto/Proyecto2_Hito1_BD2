from nltk.stem import SnowballStemmer

class Operators:
    dic=dict()
    def __init__(self,dic):
        self.dic=dic

    def L(self,word):
        stemmer = SnowballStemmer('spanish')
        newWord = stemmer.stem(word.lower())
        ids=self.dic[newWord]
        print("DocIds for",word,":",ids)
        return ids
        
            
    def AND(self,list1,list2):
        answer=[]
        if len(list1) > len(list2):
            for i in list1:
                if i in list2:
                    answer.append(i)
        else:
            for i in list2:
                if i in list1:
                    answer.append(i)
        print("AND result:",answer)
        return answer


    def OR(self,list1,list2):
        answer=[]
        if len(list1) > len(list2):
            answer = list1
            for i in list2:
                if i not in answer:
                    answer.append(i)
        else:
            answer = list2
            for i in list1:
                if i not in answer:
                    answer.append(i)
        print("OR result:",answer)
        return answer

    def NOT(self,list1,list2):
        answer=[]
        answer = list1.copy()
        for i in list1:
            if i in list2:
                answer.remove(i)
        print("NOT result:",answer)
        return answer
