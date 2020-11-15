import nltk 
import json
import re
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer

class Tokens:
    original_tokens=[]
    clean_tokens=[]
    reduced_tokens=[]
    def __init__(self,tweet_text):
        self.remove_stopwords(tweet_text)

    def word_reduction(self,tokens):
        stemmer = SnowballStemmer('spanish')
        reduced_tokens = []
        for token in tokens:
            reduced_tokens.append(stemmer.stem(token))
        return reduced_tokens

    def stopwords_split(self):
        stoplist = json.load(open('stopwords.json'))['words']
        stoplist += ['¿','?','.',',',';',':','#','*','^','«','»','º','(',')','"',"''",'``','@','¡','!','/']
        return stoplist

    def replace_tokens(self,tokens):
        replace = (('â','a'),('å',''),('ą',''),('ā',''),('á',''),('à',''),('ä',''),('ã',''),('ė',''),('ê',''),('ę',''),('ē',''),('è',''),('é',''),('ë',''),('ī',''),('î',''),('į',''),('ì',''),('ï',''),('í',''),('ō',''),('ø',''),('õ',''),('ô',''),('ö',''),('ò',''),('ó',''),('û','u'),('ū',''),('ù',''),('ü',''),('ú',''),('-',''),('`',''),('º',''),('_',' '),('.',''),('…',''),('¡',''),('~',''),('||',''),('|',''),('£',''),('¿',''),('?',''),('”',''),('“',''),('–',''))
        for a,b in replace:
            tokens = tokens.replace(a,b)
        return tokens

    def remove_emoji(self,text):
        emoji_pattern = re.compile("["
            u"\U00010000-\U0010ffff"
            #u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)

    def remove_links(self,text):
        new_text = []
        for term in text:
            if not term.startswith("http"):
                new_text.append(term)
        return new_text

    def remove_stopwords(self,text):
        stoplist = self.stopwords_split()
        text = self.remove_emoji(str(text))
        text = self.replace_tokens(text)
        tokens = nltk.word_tokenize(text)
        tokens = self.remove_links(tokens)
        self.clean_tokens = tokens.copy()
        for token in tokens:
            if token in stoplist:
                self.clean_tokens.remove(token)   
        self.reduced_tokens = self.word_reduction(self.clean_tokens)
