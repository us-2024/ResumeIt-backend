from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


class Content(BaseModel):
    content: str


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


# @app.post("/summarize/content")
# async def get_content_summary(Content: Content):
#     # Strip whitespaces and check if the content is not empty
#     Content = Content.content.strip()
#     if not Content:
#         raise HTTPException(400, "Invalid/Blank Content")
#     try:
#         # Use the generate_summary function from the summarizer module to generate a summary of the content
#         return {'Results': [{"Summary": generate_summary(Content)}]}
#     except Exception as e:
#         raise HTTPException(500, f"Internal Error: {e}")

# # Endpoint for summarizing search queries


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
