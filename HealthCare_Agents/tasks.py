from crewai import Task
from tools import tool
from agents import doc_fetcher,agent2,agent3,agent4,agent5,agent6,agent7

# Research task
research_task = Task(
    description=(
        """Fetch the top literature from databases like PubMed, arXiv, and bioRxiv for {query}.\n"""
        ),
    expected_output="""For each literature, provide a comprehensive paragraph summarizing the key details,\n
                    Ensure coverage includes both major and local sources.\n
                    including the main things, its significance, and any relevant context.""",
    tools=[tool],
    agent=doc_fetcher,
)
molecular_genetic_task = Task(
    description=(
        """Analyze the documents and extract insights related to genomic variations, protein structures, and CRISPR-based technologies for {query}.\n"""
    ),
    expected_output="""Summarize key molecular findings in a clear paragraph format.\n
                      Include gene/protein names, CRISPR functions, and potential implications for therapy or diagnostics.""",
                      
    agent=agent2,
)
drug_target_task = Task(
    description=(
        """Analyze the provided research content to identify drug-target interactions and mechanisms of action for {query}.\n"""
    ),
    expected_output="""Present a paragraph for each key interaction found.\n
                      Mention the compound, target protein, type of interaction, and known biological mechanism or pathway involved.""",

    agent=agent3,
)
adverse_event_task = Task(
    description=(
        """Scan the literature and reports to identify recent adverse drug events, safety signals, or regulatory warnings for {query}.\n"""
    ),
    expected_output="""Summarize key findings into concise paragraphs.\n
                      Include drug names, reported side effects, frequency, severity, and sources (e.g., FDA warnings, FAERS).""",
                      
    agent=agent4,
)
biomarker_discovery_task = Task(
    description=(
        """Analyze documents to discover biomarkers across genomics, proteomics, and metabolomics datasets relevant to {query}.\n"""
    ),
    expected_output="""For each biomarker, provide a paragraph summarizing its type, disease relevance, and diagnostic/prognostic value.\n
                      Highlight any personalized treatment implications.""",

    agent=agent5,
)
ip_monitoring_task = Task(
    description=(
        """Review the data and extract recent patents, IP filings, and licensing deals related to {query}.\n"""
    ),
    expected_output="""List and summarize key patents or legal events in paragraph form.\n
                      Include patent title, inventors, organizations, filing date, and purpose.""",

    agent=agent6,
)
regulatory_compliance_task = Task(
    description=(
        """Analyze updates from FDA, EMA, WHO, and ICH relevant to {query}, focusing on drug approval and compliance frameworks.\n"""
    ),
    expected_output="""Summarize new or updated guidelines in concise paragraphs.\n
                      Include the agency name, policy change, affected processes, and implications for research or clinical trials.""",

    agent=agent7,
)
