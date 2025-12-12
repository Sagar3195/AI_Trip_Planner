#Create Web Search Tool 
from crewai.tools import tool 
from langchain_community.tools import DuckDuckGoSearchResults 
import json 

@tool 
def search_web_tool(query: str):
  """
  Searches the web and return the results.
  """
  search_tool = DuckDuckGoSearchResults(num_results=10, verbose= True)
  return search_web_tool.run(query)



# Web scraping tool
#web_search_tool = WebsiteSearchTool()
#scrape_website_tool = ScrapeWebsiteTool()