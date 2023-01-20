import collections
from wsgiref import validate
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

class resume:
    def __init__(self,Mongo_db_collection_object):
        self.db = Mongo_db_collection_object
        
    def add_resume(self,user_id,json):
        resume = {
            "user_id":user_id
        }
        record = self.db.insert_one(resume)
        return resume['_id']
    
    def get_info(self,user_id):
        resume = self.db.find({"user_id" : user_id})
        return resume


    def delete_resume(self,resume_id):
            self.db.delete_one({"_id" : ObjectId(resume_id)})
            
    def update_resume(self,resume_id,json):
        Collection.update_many(
        {"_id" : ObjectId(resume_id)},
        {
                "$set":{
                        
                        },
                "$currentDate":{"lastModified":True}
                
                }
        )

