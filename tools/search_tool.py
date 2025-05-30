import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch

# Load environment variables (TAVILY_API_KEY)
load_dotenv()

# Initialize Tavily search tool
search_tool = TavilySearch(
    max_results=5,
    topic="general",
    search_depth="basic"
)