#Create LLM model 
from dotenv import load_dotenv 
from crewai import LLM
from crewai import Agent
from TravelTools import search_web_tool 
import os

load_dotenv()
groq_api_key = os.environ["GROQ_API_KEY"]
llm = LLM(
        model=  "groq/llama-3.3-70b-versatile",
        temperature=0,
        api_key= groq_api_key,
      )

#Create Agents 
 
#Agent Researcher 
guide_expert= Agent(
        role= "City Local Guide Expert",
        goal= "Provides information on things to do in the city based on the user's intersts.",
        backstory= """A local expert with a passion for sharing the best experiences and hidden gems of their city.""",
        tools= [search_web_tool],
        verbose= True,
        max_iter= 5,
        llm= llm,
        allow_delegation= False,
)


#Agent city expert 
location_expert = Agent(
    role= "Travel Trip Expert",
    goal="Adapt to the user destination vity language (French if city in French Country. Gather helpful information about to the city and city during travel.",
    backstory="""A seasoned traveler who has explored various destinations and knows the ins and outs of travel logistics.""",
    tools= [search_web_tool],
    verbose= True,
    max_iter= 5,
    llm = llm,
    allow_delegation= False,
)

#Planeer Expert Agent 
planner_expert = Agent(
    role= "Travel Planning Expert",
    goal="Compiles all gathered information to provide a comprehensive travel plan.",
    backstory="""
    You are a professional guide with a passion for travel.
    An organizational wizard who can turn a list of possibilities into a seamless itinerary.
    """,
    tools= [search_web_tool],
    verbose= True,
    max_iter= 5,
    llm = llm,
    allow_delegation= False,
)

