from bson.objectid import ObjectId
from uuid import uuid4

class resume:
    def __init__(self,Mongo_db_collection_object):
        self.db = Mongo_db_collection_object
        
    def add_resume(self,user_id,template_id,json):
        resume_id = str(uuid4())
        experience = []
        education = []
        certifications = []
        languages = []
        
        for ele in json.experience:
            doc = {
                "company_name":ele["company_name"],
                "location":ele["location"],
                "from_month":ele["from_month"],
                "from_year":ele["from_year"],
                "to_month":ele["to_month"],
                "to_year":ele["to_year"],
                "description":ele["description"]
            }
            experience.append(doc)
            
        for ele in json.education:
            doc = {
                "institute_name":ele["institute_name"],
                "course_name":ele["course_name"],
                "from_month":ele["from_month"],
                "from_year":ele["from_year"],
                "to_month":ele["to_month"],
                "to_year":ele["to_year"],
                "present":ele["present"],
                "description":ele["description"]
            }
            education.append(doc)
            
        for ele in json.certifications:
            doc = {
                "name":ele["name"],
                "url":ele["url"]
            }
            certifications.append(doc)
            
        for ele in json.languages:
            doc = {
                "name":ele["name"],
            }
            languages.append(doc)
        
        doc = {
            "personal":{
                "name":json.personal.name,
                "email":json.personal.email,
                "phone_number":json.personal.phone_number,
                "address":json.personal.address,
                "about":json.personal.about
            },
            "experience":experience,
            "education":education,
            "certifications":certifications,
            "languages":languages
        }
        resume = {
            "_id":resume_id,
            "user_id":user_id,
            "template_id":template_id,
            "data": doc
        }
        record = self.db.insert_one(resume)
        return resume['_id']
    
    def get_info(self,user_id):
        resume = list(self.db.find({"user_id" : user_id}))
        return resume
    
    def get_resume(self,resume_id):
        resume = self.db.find({"_id" : resume_id})[0]
        return resume

    def delete_resume(self,resume_id):
            self.db.delete_one({"_id" : resume_id})
            
    def update_resume(self,resume_id,json):
        self.db.update_many(
        {"_id" : resume_id},
        {
                "$set":{
                        
                        },
                "$currentDate":{"lastModified":True}
                
                }
        )

