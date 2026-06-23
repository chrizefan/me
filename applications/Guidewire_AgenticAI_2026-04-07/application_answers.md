# Application Answers — Guidewire: Senior Software Engineer, Agentic AI

## Why Guidewire / Why this role?

Guidewire has built the dominant platform for P&C insurance, and the move to production agentic AI on top of that data foundation is exactly where serious AI engineering gets interesting. Insurance documents are dense, structured, and high-stakes, and building RAG pipelines and multi-agent systems that work reliably at that fidelity level is a harder problem than most AI roles. The technical requirements map almost exactly to what I have built at PSP Investments over the last two years.

## Tell us about yourself

I am a Senior AI Engineer at PSP Investments (~$300B AUM), where I built the Virtual Analyst Platform from scratch: a production multi-agent AI system running on LangGraph, LiteLLM, Azure AI Search, and Databricks, used daily by over 100 investment analysts. I own the full stack from the FastAPI backend and RAG pipeline to the Gradio interface and Databricks observability layer. I also built the AlphaScience SDK, a unified abstraction over OpenAI, Gemini, and Claude APIs with routing and tracing. The system was selected for a live demo at the Databricks Data and AI Summit. I am an EU citizen relocating to Italy in June 2026, looking for a remote senior role in production agentic AI.

## Describe your experience with multi-agent systems and RAG

At PSP, I designed a LangGraph-based multi-agent architecture where a routing agent dispatches to specialized sub-agents with distinct tool sets, memory scopes, and retrieval strategies. The RAG layer uses Azure AI Search with hybrid semantic and keyword retrieval, embedding management, document-aware chunking for dense financial texts, and retrieval-time re-ranking. I implemented agentic loops with AsyncIO, concurrency control, timeout handling, and graceful degradation for real-time analyst queries. I route across OpenAI, Gemini, and Claude APIs via LiteLLM, and use Databricks for LLM observability and tracing.

## Greatest professional achievement

Building the Virtual Analyst Platform solo from prototype to 300 registered users and 100 active recurring analysts at a $300B pension fund, in under two years, with no unplanned outages. The platform reduced research cycle times by roughly 10x for the analysts who adopted it fully. It was selected for a live demo at the Databricks Data and AI Summit, which was PSP's first presentation of production AI work at a major industry conference.

## Why are you leaving your current role?

I am relocating from Montreal to Italy on June 1, 2026, which means transitioning out of my current position. I am looking for a remote-first senior role in Europe where I can continue doing production agentic AI engineering, ideally in a domain with high data fidelity requirements and real operational complexity.

## Note on EU remote eligibility

This role's remote/EU eligibility is not confirmed in the job posting. Confirm with Guidewire recruiting before advancing.

---
*Salary question — fill this in yourself: EUR 90,000–130,000 depending on scope and level.*
