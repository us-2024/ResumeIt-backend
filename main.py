from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


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
    experience:list[Experience]
    education: list[Education]
    Certifications: list[Certifications]
    Languages: list[Languages]
    
    
    
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


@app.post("/summarize/content")
async def get_content_summary(resume: resume):
    # Strip whitespaces and check if the content is not empty
    Content = Content.content.strip()
    # if not Content:
    #     raise HTTPException(400, "Invalid/Blank Content")
    try:
        # Use the generate_summary function from the summarizer module to generate a summary of the content
        return {'Results': True}
    except Exception as e:
        raise HTTPException(500, f"Internal Error: {e}")

# Endpoint for summarizing search queries


# @app.get("/summarize/query")
# async def get_query_summary(Query: str):
#     # Clean the query and check if the query is not empty
#     query = clean_search_query(Query)
#     if not query:
#         raise HTTPException(400, "Invalid/Blank Query")
#     try:
#         # Use the eecrawler class to scrape data related to the query
#         blogs = eecrawler.scraper(query)
#         # Generate a summary for each item of scraped data
#         for blog in blogs:
#             blog.update({'Summary': generate_summary(blog.pop('Content'))})
#         # Return the summaries of scraped data
#         return {'Results': blogs}
#     except Exception as e:
#         raise HTTPException(500, f"Internal Error: {e}")

# # Endpoint for summarizing text from a URL


# @app.get("/summarize/url")
# async def get_url_summary(URL: str):
#     # Strip whitespaces and check if the URL is valid
#     url = URL.strip()
#     if not urlparse(url).scheme:
#         raise HTTPException(400, "Invalid URL")
#     try:
#         # Use the urlcrawler class to scrape text from the provided URL
#         content = urlcrawler.sraper(url)
#         # Use the generate_summary function to generate a summary of the scraped text
#         return {'Results': [{"Summary": generate_summary(content)}]}
#     except Exception as e:
#         raise HTTPException(500, f"Internal Error: {e}")
