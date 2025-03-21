# Gemini SQL Query Retrieval App

This project is a full-stack application that integrates a natural language interface with a PostgreSQL database. The app uses Google's Gemini generative AI to convert user-friendly questions into SQL queries and then retrieves data from an industry database. It is built using Streamlit for the web interface and Python scripts for database operations.

---

## Features

- **Natural Language to SQL Conversion**:  
  Use Google's Gemini generative AI to convert plain English questions into executable SQL queries.

- **Interactive Web Interface**:  
  A user-friendly Streamlit app that accepts questions, displays responses, and shows retrieved data.

- **Database Management**:  
  A separate Python script manages the PostgreSQL database, creating and populating `employee` and `department` tables.

- **Modular Codebase**:  
  Organized into separate modules for the app interface (`app.py`), database operations (`sql.py`), and dependency management (`requirements.txt`).

---

## Requirements

- Python 3.7+
- PostgreSQL database server
- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://developers.generativeai.google/) (Gemini)
- [python-dotenv](https://pypi.org/project/python-dotenv/) for environment variable management
- [psycopg2](https://pypi.org/project/psycopg2/) for PostgreSQL connectivity

See the `requirements.txt` for a complete list of Python package dependencies.  
:contentReference[oaicite:0]{index=0}&#8203;:contentReference[oaicite:1]{index=1}

---

## Setup Instructions

1. **Clone the Repository**  
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/gemini-sql-app.git
   cd gemini-sql-app
---

Create a Virtual Environment
It is recommended to use a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
Install Dependencies
Install the required Python packages using:

bash
Copy
Edit
pip install -r requirements.txt
​

Set Up Environment Variables
Create a .env file in the project root and add your Google API key:

env
Copy
Edit
GOOGLE_API_KEY=your_google_api_key_here
This file is used by python-dotenv to load environment variables.

Configure the PostgreSQL Database

Ensure PostgreSQL is installed and running.
Update the connection details (database name, user, password, host) in both app.py and sql.py as needed.
Run the sql.py script to create and populate the necessary tables:
bash
Copy
Edit
python sql.py
​

Usage
Run the Streamlit App
Start the application using:

bash
Copy
Edit
streamlit run app.py
​

Interact with the App

Enter your natural language question in the input field.
Click the "Ask the question" button.
The app will use Gemini to convert your question into a SQL query, execute it against the PostgreSQL database, and display the result.
Review the Database Operations
The sql.py script handles:

Dropping and creating the employee and department tables.
Inserting sample data into these tables.
Displaying the data to verify successful insertion.​
File Structure
app.py
Contains the Streamlit application code that handles user input, invokes Google’s Gemini model to generate SQL queries, and retrieves data from the database.
​

sql.py
Manages PostgreSQL database operations including table creation, data insertion, and data retrieval for the employee and department tables.
​

requirements.txt
Lists all the Python package dependencies needed to run the project.
​
