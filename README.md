GenAI Market Research Automation

Multi-Agent System using CrewAI, Gemini, and Web Search

🔗 Repository: https://github.com/mohammadpakdoust/genai-market-research

Overview

This project implements a multi-agent Generative AI system that automates end-to-end market research and strategic analysis for a given company domain.

The system combines:

Large Language Models (LLMs) for reasoning and synthesis

Live web search for up-to-date, factual information

Agent orchestration to separate research and analysis responsibilities

The output is a business-ready market research report that includes an executive summary, SWOT analysis, and actionable strategic recommendations.

Key Features

🔍 Live market research using real-time web search

🤖 Multi-agent architecture (Research Agent + Analyst Agent)

🧠 LLM-driven synthesis with low-temperature, factual outputs

📄 Structured business reports generated in Markdown

🔐 Secure API key handling via environment variables

System Architecture
Agents

Research Agent

Gathers current, factual information using a web search tool

Focuses on:

Company overview

Products and services

Target customers and market

Recent developments (last 6–12 months)

Competitive landscape

Analyst Agent

Consumes the research output

Produces a strategic report including:

Executive summary

SWOT analysis

Strategic recommendations

This separation mirrors real-world workflows between market research and business strategy teams.

Technology Stack

Python 3.11+

CrewAI – multi-agent orchestration framework

Google Gemini – Large Language Model (LLM)

Serper – live web search API

uv – fast Python package management

YAML – configuration for agents and tasks

Project Structure
genai-market-research/
│
├── main.py                  # Application entry point
├── config/
│   ├── agents.yaml          # Agent roles and behavior
│   └── tasks.yaml           # Task definitions
│
├── output/                  # Generated reports (excluded from git)
├── .env                     # API keys (excluded from git)
├── .gitignore
├── pyproject.toml
└── README.md

Getting Started
1. Install Dependencies

This project uses uv for fast and reliable dependency management.

uv add "crewai[google-genai]" crewai-tools python-dotenv pyyaml

2. Configure Environment Variables

Create a .env file in the project root:

GEMINI_API_KEY=your_gemini_api_key
SERPER_API_KEY=your_serper_api_key


API keys are never committed to version control.

3. Run the Application
uv run python main.py shopify.com


Replace shopify.com with any company domain you want to analyze.

Output

The system generates a professional market research report:

output/shopify_com_market_research_report.md


Each report includes:

Executive Summary

Market and Product Overview

Competitive Landscape

SWOT Analysis

Strategic Recommendations

Engineering & GenAI Concepts Demonstrated

Transformer-based LLM inference

Prompt engineering through structured agent roles and task definitions

Tool-augmented generation (LLM + live web search)

Multi-agent task decomposition

Deterministic, low-temperature outputs for business use

Separation of concerns in AI system design

Use Cases

Automated market research

Competitive analysis

Business intelligence summaries

Strategy and decision-support tools

Demonstrations of multi-agent GenAI architectures

Background

This project was developed in a graduate-level academic context and is structured to reflect industry-grade engineering practices and real-world applicability of Generative AI systems.

Author

Mohammad Pakdoust
Graduate Student – Computing & Data Analytics
📍 Halifax, Nova Scotia, Canada

Optional Enhancements

Potential future improvements include:

Adding visual system architecture diagrams

Supporting multiple LLM providers

Exporting reports to PDF or DOCX

Caching search results to reduce API usage
