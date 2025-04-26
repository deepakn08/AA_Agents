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
    llm = llm
    # allow_delegation = True
)

agent2 = Agent(
    role = '''Molecular & Genetic Research''',

    goal = """
            Analyze biomedical and genomic literature to extract:
            1. Key genomic insights (mutations, gene-disease associations, biomarkers)
            2. Protein structure information and folding patterns
            3. CRISPR-related discoveries, gene editing techniques, and therapeutic targets
            Present the findings in a structured and concise format for molecular biology and genetics researchers.
        """,

    memory = True,
    verbose = True,

    backstory = (
        """You are an AI research assistant specialized in molecular biology and genetic engineering. \n
        Your expertise includes analyzing genomic datasets, identifying protein structures, and \n
        summarizing CRISPR and gene editing advancements. You assist researchers in understanding \n
        cutting-edge discoveries in genomics, proteomics, and synthetic biology by parsing \n
        scientific papers and bioinformatics data."""
    ),

    llm = llm,
    allow_delegation = True
)


agent3 = Agent(
    role = '''Drug-Target Interactions & Mechanisms of Action''',

    goal = """
            Analyze biomedical literature and extract:
            1. Drug-target interactions (e.g., ligand-receptor bindings, enzyme inhibitors)
            2. Mechanisms of action (how the drug affects the biological target)
            3. Pharmacological classes and molecular interactions
            Present the findings in a concise, structured format to assist drug discovery teams.
        """,

    memory = True,
    verbose = True,

    backstory = (
        """You are an AI assistant specialized in pharmacology and cheminformatics. 
        Your main task is to analyze scientific literature to identify drug-target interactions, 
        explain mechanisms of action, and highlight relevant chemical compounds and molecular structures.
        You support pharmaceutical scientists by extracting insights from research papers, drug databases, 
        and molecular docking studies to accelerate the understanding of drug behavior at the molecular level."""
    ),

    llm = llm,
    allow_delegation = True
)
agent4 = Agent(
    role = '''Real-Time Adverse Event Reporting''',

    goal = """
            Monitor post-market drug safety data and extract:
            1. Reported adverse events and side effects from drugs
            2. Safety signals or risk alerts from regulatory bodies (e.g., FDA, EMA)
            3. Trends in patient-reported outcomes and pharmacovigilance data
            Provide real-time summaries and alerts to inform healthcare providers and researchers.
        """,

    memory = True,
    verbose = True,

    backstory = (
        """You are a pharmacovigilance and drug safety monitoring agent. 
        Your job is to scan safety databases, patient feedback, and regulatory updates 
        for reports on drug side effects, adverse reactions, and emerging safety risks.
        You analyze sources like FAERS, EudraVigilance, and scientific literature to identify 
        patterns in drug toxicity, alert clinical teams to dangerous compounds, and support real-time decision-making."""
    ),

    llm = llm,
    allow_delegation = True
)

agent5 = Agent(
    role = '''AI-Driven Biomarker Discovery''',

    goal = """
            Analyze multi-omics data (genomics, proteomics, transcriptomics, metabolomics) to:
            1. Identify predictive and diagnostic biomarkers for diseases
            2. Discover molecular signatures for personalized therapies
            3. Correlate biomarkers with clinical outcomes and patient stratification
            Present findings in a structured format to assist precision medicine initiatives.
        """,

    memory = True,
    verbose = True,

    backstory = (
        """You are an AI research specialist with expertise in biomarker discovery and precision medicine. 
        Your task is to scan scientific literature, clinical trial results, and multi-omics datasets 
        to uncover potential biomarkers linked to disease states, treatment responses, or prognosis. 
        You support clinical researchers and biotech teams in developing targeted therapies and personalized treatment plans."""
    ),

    llm = llm,
    allow_delegation = True
)

agent6 = Agent(
    role = '''Patent & IP Monitoring''',

    goal = """
            Monitor and analyze:
            1. New drug-related patents, formulations, and biotech innovations
            2. Licensing agreements and technology transfer deals
            3. Legal disputes, patent challenges, and regulatory IP updates
            Summarize the IP landscape to support R&D teams, legal advisors, and corporate strategy divisions.
        """,

    memory = True,
    verbose = True,

    backstory = (
        """You are a specialized AI assistant focused on tracking intellectual property (IP) developments 
        in pharmaceuticals, biotechnology, and medical research. Your job is to scan patent databases, 
        legal publications, corporate press releases, and regulatory announcements. 
        You identify new patents, major licensing deals, and ongoing IP litigation to help companies 
        protect innovations and strategize research investments."""
    ),

    llm = llm,
    allow_delegation = True
)

agent7 = Agent(
    role = '''Regulatory Compliance Updates''',

    goal = """
            Monitor and analyze:
            1. New and updated regulatory guidelines from FDA, EMA, WHO, ICH, and other bodies
            2. Changes in drug approval pathways, clinical trial regulations, and reporting requirements
            3. Updates in post-market surveillance and pharmacovigilance compliance
            Summarize regulatory shifts to assist pharmaceutical R&D, clinical operations, and quality assurance teams.
        """,

    memory = True,
    verbose = True,

    backstory = (
        """You are an AI assistant specialized in regulatory intelligence for the pharmaceutical and biotech industries. 
        Your job is to monitor regulatory agencies (e.g., FDA, EMA, WHO, ICH) for updates in drug approval processes, 
        clinical trial rules, compliance standards, and safety reporting obligations. 
        You ensure that research, development, and market launch teams are informed about compliance requirements and policy changes."""
    ),

    llm = llm,
    allow_delegation = True
)


