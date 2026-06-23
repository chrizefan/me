# Application Answers — Aptus.AI: Senior AI Engineer

## Why do you want to work at Aptus.AI?
Legal and compliance AI is one of the harder applied AI problems: the outputs need to be grounded, traceable, and reliable in ways that matter to professional users. That's exactly the constraint I've been working under at PSP Investments, where investment analysts depend on the platform I built for daily research. Aptus.AI's focus on building AI that legal professionals actually trust is technically interesting for the same reasons — the problem isn't just making something work, it's making something professionals will stake decisions on. The multi-agent orchestration architecture you describe (specialized sub-agents, routing, state management) is also the architecture I've built in production, so the technical ramp-up would be minimal.

## Tell us about yourself
I'm a Senior AI Engineer at PSP Investments, where I've spent two years building the Virtual Analyst Platform end-to-end. The platform routes investment research queries through specialized LangGraph agents, manages state across multi-turn workflows, and synthesizes structured outputs from retrieval over Azure AI Search and Databricks. It serves 300 users with 100 active recurring analysts and was selected for a live demo at the Databricks Data & AI Summit. I also built digithings.ai, an open-source modular multi-agent AI toolkit, as a side project. I work in Python primarily (TypeScript is a gap I'm working on), and I'm an EU citizen relocating to Italy on June 1.

## Describe your experience building multi-agent systems for complex domain use cases
The core of the VAP is a multi-agent LangGraph graph that handles investment research end-to-end. When a query comes in, the orchestration layer decides whether it needs fast single-step retrieval (a direct lookup) or a deeper iterative path (multi-step research with synthesis). Specialized sub-agents handle document retrieval (Azure AI Search), structured data (Databricks), and synthesis. I've built memory persistence for multi-turn workflows, tool execution with guardrails, and structured output layers that return results in formats analysts can act on directly. The architecture is modular enough that we added new agents and data sources without rewiring the graph.

## Greatest professional achievement
Building the Virtual Analyst Platform at PSP Investments from zero to production with 300 users and 100 active recurring analysts. The platform reduced the typical research cycle by roughly 10x and was selected for a live demo at the Databricks Data & AI Summit. What made it meaningful technically was getting the agentic architecture right: the routing logic, state management, and output grounding held up in a production environment with real investment professionals relying on it daily.

## Why are you leaving your current role?
Relocating from Montreal to Italy on June 1, 2026. My PSP role is Montreal-based, so I'm looking for a remote position in Europe.

## Salary expectations
*Salary question — fill this in yourself: EUR 90,000–130,000 depending on scope and level.*
