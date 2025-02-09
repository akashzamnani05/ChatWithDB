import streamlit as st
from query_handler import execute_sql
import pandas as pd
from download import down
import os 
import os



def main():

    file_name = "mistral-7b-instruct-v0.2.Q3_K_M.gguf" 

    if(os.path.exists((file_name))):
        print("File Found")
    else:
        down()

    
    st.title('Chat With SQL')
    
    data1 = [
        (1, "Alice", "Sales", 50000, "2021-01-15"),
        (2, "Bob", "Engineering", 70000, "2020-06-10"),
        (3, "Charlie", "Marketing", 60000, "2022-03-20")
    ]
    df1 = pd.DataFrame(data1, columns=["ID", "Name", "Department", "Salary", "Hire Date"])

    data2 = [
        (1, "Sales", "Alice"),
        (2, "Engineering", "Bob"),
        (3, "Marketing", "Charlie")
    ]
    df2 = pd.DataFrame(data2, columns=["ID", "Department", "Name"])
    
    st.write("### Employee Table")
    st.dataframe(df1)
    
    st.write("### Department Table")
    st.dataframe(df2)
    text_input = st.text_area("Enter your text:")
    
    if st.button("Submit"):
        if text_input:
            result = execute_sql(text_input)
            st.write(result)
        else:
            st.warning("Please enter some text before submitting.")



if __name__ == "__main__":
    main()

    


