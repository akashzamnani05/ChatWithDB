import sqlite3
from langchain.llms import LlamaCpp
from langchain.prompts import PromptTemplate

import pandas as pd
import re

a = 'https://drive.google.com/file/d/1uIWd4DvU5AIPh0QuX_YPpl9uq33P5f5o/view?usp=sharing'

llm = LlamaCpp(model_path="./mistral-7b-instruct-v0.2.Q3_K_M.gguf", n_ctx=2048, temperature=0.1)

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

template = """
You are an expert in SQL. Convert the natural language query into an SQL query based on the given schema.
Don't complicate the query using joins; you will be asked basic SQL statements to find records.
Don't write the word sql before answer.

Schema:
1. Employees (ID, Name, Department, Salary, Hire_Date)
2. Departments (ID, Name, Manager)

User: {query}
SQL:
"""


prompt = PromptTemplate(template=template, input_variables=["query"])

def generate_sql(user_query):
    final_prompt = prompt.format(query=user_query)
    sql_query = llm(final_prompt).strip()
    
    return sql_query

def clean_text(text):
    if isinstance(text, str):
        return re.sub(r"^[\"'`]+|[\"'`]+$", '', text.strip()) # Remove leading/trailing quotes
    return text  

def execute_sql(query):
    sql_query = generate_sql(query)
    clean_query = clean_text(sql_query)
    print(clean_query)
    try:
        cursor.execute(clean_query.title())
        results = cursor.fetchall()
        print(results)
        # if not results:
        #     return 'No records found'
        # else:
            # if len(results[0]) == 5:
            #     return pd.DataFrame(results, columns=['ID', 'Name', 'Department', 'Salary', 'Hire_Date'])
            # elif len(results[0]) == 1:
            #     return results[0][0]
            # else:
            #     return pd.DataFrame(results)
            
        return pd.DataFrame(results) if results else "No records found."
    except sqlite3.Error as e:
        return f"SQL Error: {e}"



execute_sql("```sql SELECT Name FROM Departments WHERE ID = (SELECT ID FROM Departments WHERE Name = 'Sales') ) AND Manager IS NULL;'''")






