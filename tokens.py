import nltk 
import json
import re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

class Tokens:
    original_tokens=[]
    clean_tokens=[]
    reduced_tokens=[]
        
    def edit_query(self,tweet_text):
        result = []
        stoplist = self.stopwords_split()
        tweet_text = self.replace_tokens(tweet_text)
        tokens = nltk.word_tokenize(tweet_text)
        result = tokens.copy()
        for token in tokens:
            if token in stoplist:
                result.remove(token)   
        return result

    def remove_stopwords(self,text):
        stoplist = self.stopwords_split()
        text = self.remove_emoji(str(text))
        text = self.replace_tokens(text)
        text = self.remove_links(text)
        tokens = nltk.word_tokenize(text)
        self.clean_tokens = tokens.copy()
        for token in tokens:
            if token in stoplist:
                self.clean_tokens.remove(token)   
        self.reduced_tokens = self.word_reduction(self.clean_tokens)

    def word_reduction(self,tokens):
        stemmer = SnowballStemmer('spanish')
        reduced_tokens = []
        for token in tokens:
            reduced_tokens.append(stemmer.stem(token))
        return reduced_tokens

    def stopwords_split(self):
        stoplist = json.load(open('stopwords.json'))['words']
        stoplist += ['¿','?','.',',',';',':','#','*','^','«','»','º','(',')','"',"''",'``','@','¡','!','/','%','$','=','&','+','[',']',"\\",'/']
        return stoplist

    def replace_tokens(self,tokens):
        replace = (('â','a'),('å','a'),('ą','a'),('ā','a'),('á','a'),('à','a'),('ä','a'),('ã','a'),('ė','e'),('ê','e'),('ę','e'),('ē','e'),('è','e'),('é','e'),('ë','e'),('ī','i'),('î','i'),('į',''),('ì','i'),('ï','i'),('í','i'),('ō','o'),('ø','o'),('õ','o'),('ô','o'),('ö','o'),('ò','o'),('ó','o'),('û','u'),('ū','u'),('ù','u'),('ü','u'),('ú','u'),('ñ','n'),('-',''),('`',''),('º',''),('_',''),('.',''),('…',''),('¡',''),('~',''),('||',''),('|',''),('£',''),('¿',''),('?',''),('”',''),('“',''),('–',''),('*',' '),(',',' '),('=',''),('+',''),('/',''),("'",''))
        for a,b in replace:
            tokens = tokens.replace(a,b)
        return tokens

    def remove_emoji(self,text):
        emoji_pattern = re.compile("["
            u"\U00010000-\U0010ffff"
            #u"\U0001F600-\U0001F64F"
            u"\U0001F300-\U0001F5FF"
            u"\U0001F680-\U0001F6FF"
            u"\U0001F1E0-\U0001F1FF"
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)

    def remove_links(self,text):
        text = re.sub('(?:\s)http[^, ]*', '', text)
        text = re.sub('(?:\s)www[^, ]*', '', text)
        text = re.sub('(?:\s)//[^, ]*', '', text)
        pattern = r'[0-9]'
        text = re.sub(pattern, '', text)
        pattern = r'//'
        text = re.sub(pattern, '', text)
        return text