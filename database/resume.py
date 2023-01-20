import collections
from wsgiref import validate
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
CONNECTION_STRING = "mongodb+srv://cosdp:kdp1234@mflix.slvq0y2.mongodb.net/test"
client = MongoClient(CONNECTION_STRING)
dbname = client.US2024
Collection = dbname.resume
class user:
    def __init__(self,Mongo_db_collection_object):
        self.db = Mongo_db_collection_object
    def initialise(self,owner_email,password):
        resume = {
            "owner" : owner_email,
            "Password" : password,
            "Chatbots_id" : [],
            }
        record = Collection.insert_one(resume)
        return resume['_id']
    
    def get_info(self,user_id):
        resume = Collection.find({"_id" : ObjectId(id)})
        return resume

    def add_chatbot(self,id,password):
        owner = self.get_owner(id,password)
        if(owner != ''):
            # obj = chatbot(col_bot)
            chatbot_id = obj.initialise(owner)
            bot_list = Collection.find({"_id" : ObjectId(id)})[0]['Chatbots_id']
            bot_list.append(chatbot_id)
            Collection.update_many(
                {"_id" : ObjectId(id)},
                {
                        "$set":{
                                "Chatbots_id":bot_list
                                },
                        "$currentDate":{"lastModified":True}
                        
                        }
                )
            return chatbot_id
        else:
            return "unsucessful"
    def delete_chatbot(self,id,password,chatbot_id):
        if(self.validate(id,password) == True):
            # col_bot.delete_one({"_id" : ObjectId(chatbot_id)})
            return True
        else:
            return False
    def update_password(self,id,password,new_password):
        if(self.validate(id,password) == True):
            Collection.update_many(
            {"_id" : ObjectId(id)},
            {
                    "$set":{
                            "Password":new_password
                            },
                    "$currentDate":{"lastModified":True}
                    
                    }
            )
            return True
        else:
            return False
    def validate(self,id,password):
        registered_password = Collection.find({"_id" : ObjectId(id)})[0]['Password']
        if(registered_password == password):
            return True
        else:
            return False

obj = user(Collection)
