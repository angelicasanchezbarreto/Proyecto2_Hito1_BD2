import json

class InvertedIndexMem:            
    def get_doc_ids(self,term):    
        with open("files/indexFile.json",'r') as file:
            json_object = json.load(file)
            if term in json_object:
                return json_object[term]
            else:
                return []
    
    def get_norms(self,doc_id):
        with open("files/norms.json",'r') as file:
            json_object = json.load(file)
            return json_object[doc_id]
    
    def get_tweet(self,doc_id):
        with open("files/tweets.json",'r') as file:
            json_object = json.load(file)
            return json_object[doc_id]
    