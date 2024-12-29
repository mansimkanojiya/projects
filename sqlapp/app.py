from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import psycopg2

import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,database):
    conn=psycopg2.connect(database)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


    prompt=[
        """
        you are an expert in converting english questions to SQL query!
        the SQL database has the name industry and has the following tables 
        - employee,department with columns - emp_id, emp_name, emp_city, emp_salary
        for employee table and dept_id, dept_name, emp_id is taken as foreign key 
        from department table \n\nFor example,\nExample 1 - How many entries of
        records are present in employee table?, the SQL command will be 
        something like this SELECT COUNT(*) FROM STUDENT ;
        \nExample 2 - Tell me all the employee name working in department it?,
        the SQL command will be something like this SELECT emp_name from employee
        join department on employee.emp_id = department.emp_id where dept_name ilike
        "it";
        also the sql code should not have ''' in beginning or end and sql word in the output

        """
    ]


    st.set_page_config(page_title="I can Retrieve any sql query")
    st.header("Gemini App To Retrieve SQL Data")

    question=st.text_input("Input: ",key="input")

    submit=st.button("Ask the question")


    if submit:
        response=get_gemini_response(question,prompt)
        print(response)
        data=read_sql_query(response,"industry.database")
        st.subheader("The Response is")
        for row in data:
            print(row)
            st.header(row)
