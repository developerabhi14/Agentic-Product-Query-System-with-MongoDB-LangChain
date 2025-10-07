# Agentic Product Query System with MongoDB & LangChain

## Description
This project demonstrates an agentic, chat-based product query system built on top of a MongoDB database using LangChain agents. It allows users to interact with product data in natural language, letting an LLM reason, generate MongoDB queries, and fetch dynamic responses. The system supports:

- **Text-to-MongoDB query agents:** Ask questions like “Show all products under $50 with tag ‘smart’” and get structured results from MongoDB.
- **Retrieval-Augmented Generation (RAG):** Load product documents from MongoDB, create embeddings, and answer questions using semantic retrieval with a vector store (Chroma).
- **Dynamic, multi-field product data:** Includes diverse categories, specifications, reviews, dimensions, and optional fields to showcase LangChain’s full capabilities.

## Tech Stack

- **LangChain** – Agents, toolkit, retrieval chains
- **MongoDB** – Product database with dynamic documents
- **Chroma** – Local vector store for embeddings and RAG
- **OpenAI** – LLM & embeddings (configurable with other providers)
- **Python** – Core implementation

## Use Cases

- Chat-based product search and recommendation
- Natural language analytics on e-commerce data
- Experimenting with agentic AI workflows for databases

## Setup

1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY="your_api_key_here"
   ```
4. Run the MongoDB agent or RAG example scripts.

## Project Goal
Showcase how LangChain agents can act autonomously to query, reason, and fetch data from a real-world MongoDB database, bridging natural language queries with structured database operations.
