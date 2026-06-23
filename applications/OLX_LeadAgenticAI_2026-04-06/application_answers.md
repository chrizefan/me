# Application Answers — OLX: Lead Agentic AI Engineer

## Why do you want to work at OLX?
OLX operates at a scale where automating business functions with agentic AI can create measurable impact across thousands of interactions per day. I've spent two years building exactly this kind of system at PSP Investments — an LLM-powered platform serving investment analysts at a ~$300B AUM fund — and the technical problems OLX is solving feel like a natural next step: larger user base, broader function coverage (Finance, HR, Legal, Customer Support), and an even richer data ecosystem to build on. The stack overlap (LangGraph, Claude, OpenAI, n8n) means I can contribute immediately, and I'm interested in applying what I've learned in a high-reliability enterprise context to a global product environment.

## Tell us about yourself / Describe your background
I'm a Senior AI Engineer currently building and operating the Virtual Analyst Platform at PSP Investments, a ~$300B Canadian pension fund. Over the past two years I've designed the platform from scratch: LangGraph-based multi-agent orchestration, RAG pipelines over structured and unstructured data, a unified SDK (AlphaScience SDK) that abstracts OpenAI, Gemini, Claude, and Databricks, and a Gradio-based front end used by 300 users with 100 active recurring analysts. The system was selected for a live demo at the Databricks Data & AI Summit. I own everything from architecture through deployment and iteration, and I work in Python primarily. I'm an EU citizen relocating to Italy on June 1, fluent in English, French, and Romanian.

## Describe your experience with agentic AI systems / LLM orchestration
The Virtual Analyst Platform runs on LangGraph-based multi-agent graphs. I've built orchestration layers that handle routing between specialized agents (data retrieval, document analysis, synthesis), manage state across multi-turn workflows, implement tool use with strict guardrails, and run automated evals using LLM-as-a-judge patterns. I've also designed and built the AlphaScience SDK, which provides composable primitives for building agentic workflows on top of multiple model providers. The system processes investment research queries end-to-end with retrieval over Azure AI Search and Databricks, returning structured outputs to analysts in under a minute on most paths.

## What is your greatest professional achievement?
Building and shipping the Virtual Analyst Platform at PSP Investments from zero to 300 users and 100 active recurring analysts, with no team support on the AI engineering side for the first year. The platform reduced the research cycle for investment analysts by roughly 10x on typical queries. The system was robust enough to be selected for a live demonstration at the Databricks Data & AI Summit, which is a significant public signal of production quality. What I'm most proud of is that I made architectural decisions early (SDK-level abstractions, provider-agnostic routing, eval pipelines) that made it easy to add new capabilities without rework, and the system has been running in production without major incidents since launch.

## Why are you leaving your current role?
I'm relocating from Montreal to Italy on June 1, 2026, which makes my current on-site role in Montreal impractical to continue. I'm looking for a fully remote position in Europe where I can do the same kind of work I've been doing: building and owning production agentic AI systems end-to-end.

## Salary expectations
*Salary question — fill this in yourself: EUR 90,000–130,000 depending on scope and level.*
