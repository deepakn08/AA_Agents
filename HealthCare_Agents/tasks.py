from crewai import Task
from tools import tool
from agents import doc_fetcher

# Research task
research_task = Task(
    description=(
        """Fetch the top literature from databases like PubMed, arXiv, and bioRxiv for {query}.\n"""
        ),
    expected_output="""Combine the information from all the fetched document and create a detailed summary of the information present in the document.""",
    tools=[tool],
    agent=doc_fetcher,
)