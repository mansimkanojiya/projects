# AI Chat for Banking Transactions

This project demonstrates how to use Large Language Models (LLMs) to convert banking statement PDFs into structured data, generate and refine SQL queries, and then present user-friendly responses. It uses Python, a PostgreSQL database (managed via PGAdmin), and an LLM-based natural language interface.

---

## Flowchart Overview


1. **Input**: A PDF bank statement containing transaction data.
2. **LLM Conversion**: The LLM generates SQL queries to transform the PDF data into a tabular format.
3. **Database Processing**: The generated SQL queries are executed on a PostgreSQL database (using PGAdmin for management).
4. **Query Refinement**: The LLM refines both the user question and the query result for clarity.
5. **Output**: The final answer is returned in natural language, along with the source or context.

---

## Files

- **Banking_Chatbot.py.ipynb**  
  Contains the core Python code to:
  - Accept user queries in natural language.
  - Convert/Refine queries using an LLM.
  - Execute SQL queries on the database.
  - Return results with user-friendly explanations.

- **Flowchart.jpg**  
  Illustrates the high-level architecture of the system.

---

## Requirements

1. **Python 3.7+**
2. **Dependencies** (example):
   - `pandas`
   - `psycopg2` (for PostgreSQL connections)
   - `openai` or any other LLM integration library
   - `PyPDF2` or a similar library to handle PDF parsing
3. **PostgreSQL Database** and **PGAdmin**:
   - Ensure PostgreSQL is installed and running.
   - PGAdmin is optional but helps manage the database visually.
4. **API Keys**:
   - If using an external LLM like OpenAI, you need a valid API key.

---

Usage
Start the Notebook:

Open Banking_Chatbot.py.ipynb in Jupyter Notebook or any compatible environment.
Run the notebook cells in order.
Upload/Load a Bank Statement PDF:

The code will parse the PDF or prompt you to provide a path to the PDF file.
The LLM will generate SQL queries to structure the data.
Ask Questions:

Enter natural language queries (e.g., “What was my total expenditure last month?”).
The LLM refines the question and generates an SQL query to fetch the relevant data.
The Python script executes the query in PostgreSQL.
View Results:

The system returns the answer in a human-readable format, along with relevant sources or details from the database.


