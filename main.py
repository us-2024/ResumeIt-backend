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
import img2pdf
CONNECTION_STRING = "mongodb+srv://cosdp:kdp1234@mflix.slvq0y2.mongodb.net/test"
client = MongoClient(CONNECTION_STRING)
dbname = client.US2024
email_collection = email(dbname.email)
resume_collection = resume(dbname.resume)
class personal(BaseModel):
    name:str
    email:str
    phoneNumber:str
    address:str
    about:str
    website:str
    # Example
    class Config:
        schema_extra = {
            "example": {
                "name":"kaustub dutt pandey",
                "email":"pandeykaustubdutt@gmail.com",
                "phoneNumber":"+917405029403",
                "address":"Udaipur,Rajasthan",
                "about":"abc",
                "website":"www.github.com"
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
                "education_description":"IIT Jodhpur" 
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
    present:bool
    discription:str
    # Example
    class Config:
        schema_extra = {
            "example": {
                "institute_name":"IIT Jodhpur",
                "Course_name":"Computer science engineering",
                "from_year":"2020",
                "to_year":"2024",
                "present":False,
                "description":"IIT Jodhpur" 
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
    experience:list
    education: list
    certifications: list
    languages: list
    projects:list
    skills:list
    
    
    
    class Config:
        schema_extra = {
            "example": {
                "personal":{
                "name":"kaustub dutt pandey",
                "email":"pandeykaustubdutt@gmail.com",
                "phoneNumber":"+917405029403",
                "address":"Udaipur,Rajasthan",
                "about":"abc",
                "website":"www.github.com"
            },
                "experience":[{
                "companyName":"IIT Jodhpur",
                "jobRole":"SDE",
                "location":"Jodhpur, Rajasthan",
                "fromMonth":"2",
                "fromYear":"2020",
                "toMonth":"5",
                "toYear":"2023",
                "description":"IIT Jodhpur" 
            }],
                "education":[ {
                "instituteName":"IIT Jodhpur",
                "courseName":"Computer science engineering",
                "fromMonth":"2",
                "fromYear":"2020",
                "toMonth":"5",
                "toYear":"2024",
                "present":False,
                "description":"IIT Jodhpur" 
            }],
                "certifications":[{
                "name":"Coursera",
                "url":"www.coursera.com"
            }],
                "languages":[{
                "name":"English" 
            }],
                "projects":[{
                    "name":"project-1",
                    "url":"www.google.com",
                    "description":"this is a project"
            }],
                "skills":[{
                    "name":"hackathon"
            }]                 
            }
        } 
# Initialize FastAPI
app = FastAPI()
origins = [
    "https://resumeit-2024.vercel.app",
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


@app.get("/")
async def read_root():
    return {"Team": "US-2024"}

@app.post("/add/resume")
async def Add_Resume(resume: resume,template_id:str,user_id:str = Header()):
    try:
        resume_collection.add_resume(user_id,template_id,resume)
        return {"message":"saved successfully"} 
    except Exception as e:
        raise HTTPException(500, f"Internal Error: {e}")
    
@app.get("/resume/data")
async def Resume_data(user_id:str = Header()):
    try:
        return resume_collection.get_info(user_id)
    except Exception as e:
        return []
        print(e)
        
        
@app.get("/resume/data/show")
async def show_Resume_data(resume_id:str):
    try:
        return resume_collection.get_resume(resume_id)
    except Exception as e:
        print(e)

@app.post("/update/resume")
async def update_Resume(resume: resume,resume_id:str):
    try:
        resume_collection.update_resume(resume_id,resume)
        return {"message":"updated successfully"} 
    except Exception as e:
        raise HTTPException(500, f"Internal Error: {e}")
    
@app.delete("/resume/delete")
async def delete_resume(resume_id:str):
    try:
        resume_collection.delete_resume(resume_id)
        return {"message":"Deleted Successfully"}
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
    try:
        print(reciever_addresses)
        with open(str(user_id)+".pdf", "wb") as buffer:
            buffer.write(img2pdf.convert(file.file))
        reciever_addresses = reciever_addresses[0].split(",")
        data = email_collection.get_info(user_id)
        time.sleep(4)
        send_email(data["email"],data['password'],reciever_addresses,subject,body,[str(user_id)+".pdf"])
        os.remove(str(user_id)+".pdf")
        return {"Task":"Send Email","Status":"Success"}
    except Exception as e:
        os.remove(str(user_id)+".pdf")
        return {"Task":"Send Email","Status":"Failed","Error":str(e)}


# @app.post("/test")
# async def test(file:UploadFile):
#     with open(str("test")+".pdf", "wb") as buffer:
#         buffer.write(img2pdf.convert(file.file))