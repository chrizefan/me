# Application Answers — Percepta: Applied AI Engineer - Europe

## Why do you want to work at Percepta?
Percepta's model of embedding deeply with critical institutions and shipping AI systems that actually change workflows is the direction I want to go next. At PSP Investments I've done the internal version of this work — designing and deploying the Virtual Analyst Platform for 100 active investment analysts at a ~$300B fund — and I'm interested in applying that experience to a broader range of industries and problem types. The fact that Percepta is building Mosaic as a reusable platform alongside customer-specific delivery is appealing because it creates the same pressure to build for durability and composability that I've experienced, not just one-off integrations.

## Tell us about yourself
I'm a Senior AI Engineer at PSP Investments, where I've spent two years building and operating the Virtual Analyst Platform end-to-end. The platform handles RAG over structured and unstructured data, multi-step LangGraph agents, human-in-the-loop workflows, and a unified SDK (AlphaScience SDK) that abstracts across OpenAI, Gemini, Claude, Databricks, and Azure AI Search. It serves 300 users with 100 active analysts and was selected for a live demo at the Databricks Data & AI Summit. I've owned the full stack from architecture through production operations, which has given me a practical understanding of what it takes to build reliable AI systems in high-stakes environments. I'm an EU citizen relocating to Italy on June 1, right to work across the EU.

## Describe your experience building production LLM-powered systems
The Virtual Analyst Platform processes investment research queries end-to-end using a multi-agent LangGraph graph. Each query is routed through retrieval (Azure AI Search over company filings, market data, internal research), a synthesis agent, and a structured output layer that returns results to analysts in under a minute on most paths. I built the AlphaScience SDK to make it easy to add new model providers (OpenAI, Gemini, Claude, Databricks) without changing agent logic, and I built eval pipelines to monitor retrieval quality and output correctness in production. The system has been running reliably in a regulated financial environment since launch.

## Greatest professional achievement
Delivering the Virtual Analyst Platform from zero to production at PSP Investments without a dedicated AI engineering team. The platform went from an internal proof of concept to a system with 300 registered users and 100 active recurring analysts, reducing the typical research cycle by roughly 10x. What made it meaningful was that the system was reliable enough to be selected for a live demo at the Databricks Data & AI Summit, a public signal that the engineering held up beyond a controlled demo environment. The architectural decisions I made early (provider-agnostic SDK, composable agent graph, eval pipelines from day one) meant we could add capabilities continuously without rewrites.

## Why are you leaving your current role?
I'm relocating from Montreal to Italy on June 1, 2026. My current role at PSP Investments is Montreal-based, so I'm looking for a fully remote position in Europe where I can continue doing the same kind of applied AI engineering work.

## Salary expectations
*Salary question — fill this in yourself: EUR 90,000–130,000 depending on scope and level.*
