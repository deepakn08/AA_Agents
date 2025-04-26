import os
from crewai import Crew, Process
from tasks import research_task,molecular_genetic_task,drug_target_task,adverse_event_task,biomarker_discovery_task,ip_monitoring_task,regulatory_compliance_task
from agents import doc_fetcher,agent2,agent3,agent4,agent5,agent6,agent7
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq

llm = ChatGroq(
    model = "llama-3.3-70b-versatile",
    temperature = 0.7,
    api_key = ''
)

crew_1 = Crew(
    agents = [doc_fetcher],
    tasks = [research_task],
    process=Process.sequential
)
crew_2 = Crew(
    agents = [doc_fetcher,agent2],
    tasks = [research_task,molecular_genetic_task],
    process=Process.sequential
)
crew_3 = Crew(
    agents = [doc_fetcher,agent3],
    tasks = [research_task,drug_target_task],
    process=Process.sequential
)
crew_4 = Crew(
    agents = [doc_fetcher,agent4],
    tasks = [research_task,adverse_event_task],
    process=Process.sequential
)
crew_5 = Crew(
    agents = [doc_fetcher,agent5],
    tasks = [research_task,biomarker_discovery_task],
    process=Process.sequential
)
crew_6 = Crew(
    agents = [doc_fetcher,agent6],
    tasks = [research_task,ip_monitoring_task],
    process=Process.sequential
)
crew_7 = Crew(
    agents = [doc_fetcher,agent7],
    tasks = [research_task,regulatory_compliance_task],
    process=Process.sequential
)
# Mapping of topic keywords to crew instances
crew_map = {
    "Scientific Literature & Clinical Trials": crew_1,
    "Molecular & Genetic Research": crew_2,
    "Drug-Target Interactions & Mechanisms of Action": crew_3,
    "Real-Time Adverse Event Reporting": crew_4,
    "AI-Driven Biomarker Discovery": crew_5,
    "Patent & IP Monitoring": crew_6,
    "Regulatory Compliance Updates": crew_7
}

# Classifier prompt
topic_prompt = ChatPromptTemplate.from_template(
    """
        Classify the user query into one of the following biomedical research domains:
        - Scientific Literature & Clinical Trials
        - Molecular & Genetic Research
        - Drug-Target Interactions & Mechanisms of Action
        - Real-Time Adverse Event Reporting
        - AI-Driven Biomarker Discovery
        - Patent & IP Monitoring
        - Regulatory Compliance Updates

        Query: "{query}"

        Respond only with the exact category name.
    """
)

def search_data(query, output_dir='generated_articles'):
    # Classify the query into a topic
    chain = RunnablePassthrough() | topic_prompt | llm
    response = chain.invoke({'query':query})
    
    # Fallback to crew2 if classification fails
    crew = crew_map.get(response.content)
    
    # Run the selected crew
    result = crew.kickoff(inputs={'query': query})

    return os.path.join(output_dir, 'query_1')

search_data('What recent adverse event reports have been issued for COVID-19 vaccines?')