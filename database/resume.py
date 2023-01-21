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
        projects = []
        skills = []
        
        for ele in json.experience:
            doc = {
                "companyName":ele["companyName"],
                "jobRole":ele["jobRole"],
                "location":ele["location"],
                "fromMonth":ele["fromMonth"],
                "fromYear":ele["fromYear"],
                "toMonth":ele["toMonth"],
                "toYear":ele["toYear"],
                "description":ele["description"]
            }
            experience.append(doc)
            
        for ele in json.education:
            doc = {
                "instituteName":ele["instituteName"],
                "courseName":ele["courseName"],
                "fromMonth":ele["fromMonth"],
                "fromYear":ele["fromYear"],
                "toMonth":ele["toMonth"],
                "toYear":ele["toYear"],
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
        
        for ele in json.projects:
            doc = {
                "name":ele["name"],
                "url":ele["url"],
                "description":ele["description"]
            }
            projects.append(doc)
            
        for ele in json.skills:
            doc = {
                "name":ele["name"],
            }
            skills.append(doc)
        
        doc = {
            "personal":{
                "name":json.personal.name,
                "email":json.personal.email,
                "phoneNumber":json.personal.phoneNumber,
                "address":json.personal.address,
                "about":json.personal.about,
                "website":json.personal.website
            },
            "experience":experience,
            "education":education,
            "certifications":certifications,
            "languages":languages,
            "projects":projects,
            "skills":skills
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
        experience = []
        education = []
        certifications = []
        languages = []
        projects = []
        skills = []
        
        for ele in json.experience:
                doc = {
                    "companyName":ele["companyName"],
                    "jobRole":ele["jobRole"],
                    "location":ele["location"],
                    "fromMonth":ele["fromMonth"],
                    "fromYear":ele["fromYear"],
                    "toMonth":ele["toMonth"],
                    "toYear":ele["toYear"],
                    "description":ele["description"]
                }
                experience.append(doc)
                
        for ele in json.education:
            doc = {
                "instituteName":ele["instituteName"],
                "courseName":ele["courseName"],
                "fromMonth":ele["fromMonth"],
                "fromYear":ele["fromYear"],
                "toMonth":ele["toMonth"],
                "toYear":ele["toYear"],
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
        
        for ele in json.projects:
            doc = {
                "name":ele["name"],
                "url":ele["url"],
                "description":ele["description"]
            }
            projects.append(doc)
            
        for ele in json.skills:
            doc = {
                "name":ele["name"],
            }
            skills.append(doc)
        
        doc = {
            "personal":{
                "name":json.personal.name,
                "email":json.personal.email,
                "phone_number":json.personal.phoneNumber,
                "address":json.personal.address,
                "about":json.personal.about,
                "website":json.personal.website
            },
            "experience":experience,
            "education":education,
            "certifications":certifications,
            "languages":languages,
            "projects":projects,
            "skills":skills
        }
        self.db.update_one(
        {"_id" : resume_id},
        {
                "$set":{
                        "data":doc
                        },
                "$currentDate":{"lastModified":True}
                
                }
        )

