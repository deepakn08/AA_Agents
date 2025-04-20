import os
from crewai import Agent, LLM
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI

# google_api_key = os.getenv("GOOGLE_API_KEY")
# print(google_api_key)


llm = LLM(
    model = "gemini/gemini-2.0-flash",
    temperature = 0.7,
    api_key = ''
)

## Documents Information fetcher
doc_fetcher = Agent(
    role = '''You are an expert biomedical researcher''',
    
    goal = """Your task is to find the relevant documents and find the information from the document that you have fetched \n
                and generate the summary according the query of the quers and its requirement \n
                Compile a concise meta-analysis from multiple papers (optionally structured)""",
    memory = True,
    verbose = True,
    backstory = (
         """You are an assistant that specializes in retrieving, analyzing, and summarizing medical research \n
            literature from databases like PubMed, arXiv, and bioRxiv. You help researchers rapidly \n
            understand key insights from large volumes of scientific papers."""
    ),
    llm = llm,
    allow_delegation = True
)
