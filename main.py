from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, Header, Depends, UploadFile, BackgroundTasks,Form
from pydantic import BaseModel
from emailer_module import send_email
from database.email import *
from database.resume import *
import shutil
import time
import platform
import os
CONNECTION_STRING = "mongodb+srv://cosdp:kdp1234@mflix.slvq0y2.mongodb.net/test"
client = MongoClient(CONNECTION_STRING)
dbname = client.US2024
email_collection = email(dbname.email)
resume_collection = resume(dbname.resume)
# class send_email_data(BaseModel):
#     user_id:str
#     reciever_addresses:list[str]
#     subject:str
#     body:str 
#     class Config:
#         schema_extra = {
#             "example": {
#                 "user_id":"abcdef",
#                 "reciever_addresses":["pandeykaustubdutt@gmail.com","mitali.lohar2002@gmail.com"],
#                 "subject":"This is a test mail",
#                 "body":"hello this is a test user mail generated using smtp secure server"
#             }
#         }
class personal(BaseModel):
    name:str
    email:str
    phone_number:str
    address:str
    
    # Example
    class Config:
        schema_extra = {
            "example": {
                "name":"kaustub dutt pandey",
                "email":"pandeykaustubdutt@gmail.com",
                "phone_number":"+917405029403",
                "address":"Udaipur,Rajasthan",
                
            }
        }
class Experience(BaseModel):
    company_name:str
    location:str
    from_year:int
    to_year:int
    educationDescription:str
    # Example
    class Config:
        schema_extra = {
            "example": {
                "company_name":"IIT Jodhpur",
                "location":"Jodhpur, Rajasthan",
                "from_year":"2020",
                "to_year":"2023",
                "educationDescription":"IIT Jodhpur" 
            }
        }
class about(BaseModel):
    about :str
    
    
    # Example
    class Config:
        schema_extra = {
            "example": {
                "about":"abc"
                
                 
            }
        }          
class Education(BaseModel):
    Institute_name :str
    Course_name:str
    from_year:int
    to_year:int
    isPresentEducation:bool
    educationdiscription:str
    # Example
    class Config:
        schema_extra = {
            "example": {
                "Institute_name":"IIT Jodhpur",
                "Course_name":"Computer science engineering",
                "from_year":"2020",
                "to_year":"2024",
                "isPresentEducation":"yes",
                "educationDescription":"IIT Jodhpur" 
            }
        }      
class Certifications(BaseModel):
    name :str
    url:str
    
    # Example
    class Config:
        schema_extra = {
            "example": {
                "name":"Coursera",
                "url":"www.coursera.com"
                 
            }
        }   
        
class Languages(BaseModel):
    name :str
    
    
    # Example
    class Config:
        schema_extra = {
            "example": {
                "name":"English"
                
                 
            }
        }  
        
class resume(BaseModel):
    personal : personal
    about: about
    experience:list
    education: list
    Certifications: list
    Languages: list
    
    
    
    class Config:
        schema_extra = {
            "example": {
                "personal":{
                "name":"kaustub dutt pandey",
                "email":"pandeykaustubdutt@gmail.com",
                "phone_number":"+917405029403",
                "address":"Udaipur,Rajasthan"
            },
                "about":{ 
                    "about":"abc"
            },
                "experience":[{
                "company_name":"IIT Jodhpur",
                "location":"Jodhpur, Rajasthan",
                "from_year":"2020",
                "to_year":"2023",
                "educationDescription":"IIT Jodhpur" 
            }],
                "education":[ {
                "Institute_name":"IIT Jodhpur",
                "Course_name":"Computer science engineering",
                "from_year":"2020",
                "to_year":"2024",
                "isPresentEducation":"yes",
                "educationDescription":"IIT Jodhpur" 
            }],
                "certifications":[{
                "name":"Coursera",
                "url":"www.coursera.com"
                 
            }],
                "languages":[{
                "name":"English" 
                 
            }]
                
                
                
                
                 
            }
        } 
# Initialize FastAPI
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
]

# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crawler intializaton

# Root endpoint - returns a simple message indicating the team name


@app.get("/")
async def read_root():
    return {"Team": "US-2024"}

# Endpoint for summarizing text content


@app.post("/add/resume")
async def Add_Resume(resume: resume):
    try:
        resume_collection.add_resume()
        return {'Results': True}
    except Exception as e:
        raise HTTPException(500, f"Internal Error: {e}")
    
@app.get("resume/data")
async def Resume_data(user_id:str = Header()):
    try:
        return resume_collection.get_info(user_id)
    except Exception as e:
        print(e)
        
@app.get("/email/data")
async def get_email_password(user_id:str = Header()):
    try:
        data = email_collection.get_info(user_id)
        return data
    except Exception as e:
        print(e)
        return {}
    
@app.get("/email/data/update")
async def get_email_password(user_id:str = Header(),email:str = Header(),password:str = Header()):
    try:
        email_collection.update_email_pass(user_id,email,password)
        return True
    except Exception as e:
        print(e)
        return False

@app.get("/email/add")
async def add_email_password(user_id:str = Header(),email:str = Header(),password:str = Header()):
    try:
        email_collection.add_email_pass(user_id,email,password)
        return {"success":True}
    except Exception as e:
        return {"success":False,"error":str(e)}
    

@app.post("/sendemail")
async def email_send(file:UploadFile,user_id:str = Form(),reciever_addresses:list = Form(),subject:str = Form(),body:str = Form()):
    with open(str(user_id)+".pdf", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    reciever_addresses = reciever_addresses[0].split(",")
    print(reciever_addresses)
    data = email_collection.get_info(user_id)
    print(data)
    time.sleep(4)
    send_email(data["email"],data['password'],reciever_addresses,subject,body,[str(user_id)+".pdf"])

@app.get("/system/config")
async def sys_info():
    my_system = platform.uname()
    print(f"System: {my_system.system}")
    print(f"Node Name: {my_system.node}")
    print(f"Release: {my_system.release}")
    print(f"Version: {my_system.version}")
    print(f"Machine: {my_system.machine}")
    print(f"Processor: {my_system.processor}")