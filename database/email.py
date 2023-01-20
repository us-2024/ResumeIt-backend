import collections
from wsgiref import validate
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
CONNECTION_STRING = "mongodb+srv://cosdp:kdp1234@mflix.slvq0y2.mongodb.net/test"
client = MongoClient(CONNECTION_STRING)
dbname = client.US2024
Collection = dbname.email
class email:
    def __init__(self,Mongo_db_collection_object):
        self.db = Mongo_db_collection_object
        
    def add_email_pass(self,user_id,owner_email,password):
        if not self.db.count_documents({"user_id":user_id})>0:
            doc = {
                "user_id":user_id,
                "email" : owner_email,
                "password" : password,
                }
            record = Collection.insert_one(doc)
            return doc['_id']
        else:
            raise Exception("already_Added")
    
    def get_info(self,user_id):
        return_data ={}
        data = Collection.find({"user_id" : user_id})
        return_data["email"]=data[0]['email']
        return_data["password"]= data[0]["password"]
        # print(return_data)
        return return_data 
            
            

    def update_email_pass(self,user_id,email,password):
        Collection.update_one(
        {"user_id" : user_id},
        {
                "$set":{
                        "email" : email,
                        "password" : password,
                        },
                "$currentDate":{"lastModified":True}
                
                }
        )
