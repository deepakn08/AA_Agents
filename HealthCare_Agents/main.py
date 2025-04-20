import os
from crewai import Crew, Process
from tasks import research_task
from agents import doc_fetcher

crew = Crew(
    agents = [doc_fetcher],
    tasks = [research_task],
    process=Process.sequential
)
def search_data(query, output_dir='generated_articles'):
    result=crew.kickoff(inputs={'query':query})
    return os.path.join(output_dir, 'query_1')

search_data('What is medicine for Tuberculosis.')