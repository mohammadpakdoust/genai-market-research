# GenAI Market Research Automation
**Multi-Agent System using CrewAI, Gemini, and Web Search**

🔗 **Repository:** https://github.com/mohammadpakdoust/genai-market-research

---

## Overview

This project implements a **multi-agent Generative AI system** that automates end-to-end market research and strategic analysis for a given company domain.

The system combines:
- Large Language Models (LLMs) for reasoning and synthesis  
- Live web search for up-to-date, factual information  
- Agent orchestration to separate research and analysis responsibilities  

The output is a business-ready market research report that includes an executive summary, SWOT analysis, and actionable strategic recommendations.

---

## Key Features

- 🔍 Live market research using real-time web search  
- 🤖 Multi-agent architecture (Research Agent + Analyst Agent)  
- 🧠 LLM-driven synthesis with low-temperature, factual outputs  
- 📄 Structured business reports generated in Markdown  
- 🔐 Secure API key handling via environment variables  

---

## System Architecture

### Agents

**Research Agent**
- Gathers current, factual information using a web search tool
- Focuses on company overview, products, market, recent developments, and competitors

**Analyst Agent**
- Synthesizes research into executive summaries, SWOT analysis, and strategic recommendations

---

## Technology Stack

- Python 3.11+
- CrewAI
- Google Gemini
- Serper Web Search
- uv
- YAML configuration

---

## Author

**Mohammad Pakdoust**  
Graduate Student – Computing & Data Analytics  
Halifax, Nova Scotia, Canada
