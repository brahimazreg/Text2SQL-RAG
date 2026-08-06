# Text2SQL-RAG

A Retrieval-Augmented Generation (RAG) system that converts natural language questions into SQL queries. This project combines schema retrieval, semantic search, and LLM-powered SQL generation to provide accurate and context-aware database querying.
                                                                  
       
## 🎯 Overview

**Text2SQL-RAG** is an intelligent chatbot that translates natural language questions into SQL queries by combining:

- **Schema Retrieval**: Automatically extracts and retrieves relevant database tables and columns
- **Semantic Search**: Finds similar examples and relevant context from a vector database
- **LLM Generation**: Uses Google's Gemini models to generate SQL queries
- **SQL Validation**: Checks generated queries for safety, correctness, and reliability

The goal is to make database querying accessible by allowing users to interact with databases using natural language instead of writing SQL manually.

---

## ✨ Features

- 🔍 **Intelligent Schema Discovery**
  - Automatically identifies relevant tables and columns
  - Provides database context to the language model

- 🤖 **RAG-Based SQL Generation**
  - Combines retrieval with LLM reasoning
  - Improves SQL accuracy using relevant examples

- 🛡️ **SQL Validation**
  - Detects invalid queries
  - Helps prevent unsafe SQL execution

- 🔎 **Semantic Search**
  - Retrieves similar SQL examples using vector embeddings

- 🐳 **Docker Support**
  - Easy deployment and environment setup

- 🔄 **Modular Architecture**
  - Separate components for retrieval, generation, validation, and database interaction

---

## 🏗️ Architecture

```text
User Question
      |
      v
🔍 Schema Retrieval + Semantic Search
      |
      v
🤖 Gemini LLM SQL Generation
      |
      v
✅ SQL Validation
      |
      v
💾 Database Execution
      |
      v
Final Answer

---
 

## 📁 Project Structure

```text
Text2SQL-RAG/
│
├── sql_rag_chatbot/
│   ├── __init__.py
│   ├── database.py          # Database connection management
│   ├── schema_loader.py     # Database schema extraction
│   ├── retriever.py         # Semantic retrieval component
│   ├── sql_generator.py     # LLM-based SQL generation
│   ├── validator.py         # SQL validation and safety checks
│   └── agent.py             # Main RAG workflow orchestration
│
├── tests/
│   ├── test_db.py
│   └── test_gemini.py
│
├── main.py                  # CLI entry point
├── app.py                   # Application interface
├── config_base.py           # Configuration settings
├── requirements.txt
├── pyproject.toml
├── Dockerfile
└──.dockerignore

## 🚀 Installation

git clone https://github.com/brahimazreg/Text2SQL-RAG.git

cd Text2SQL-RAG

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

## ▶️ How It Works

The system will:

Receive a natural language question
Retrieve relevant database schema information
Search for similar SQL examples
Generate SQL using Gemini
Validate the SQL query
Execute the query
Return the result

## 🐳 Docker

Build the image:

```bash
docker build -t text2sql-rag .

docker run --env-file .env text2sql-rag

```markdown
## 💡 Example

### User Question

Who spent most money ?


```markdown
## 🔐 Configuration

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
DATABASE_URL=your_database_connection_string

🧰 Technologies Used
Python
Google Gemini
LangChain
SQLAlchemy
Vector Database / Embeddings
SQL Server
Docker

📄 License

This project is licensed under the MIT License
Author :  AZREG BRAHIM

  



   












