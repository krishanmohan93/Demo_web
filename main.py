import streamlit as st
import pandas as pd

st.title("My First Website")
st.header("Python")
st.subheader("java")
st.markdown("I love Python ")
st.code("""for i in range(1:5,1):
        print("Hello")  """)
dataset = pd.read_csv("tmdb_5000_movies.csv")
st.dataframe(dataset)

name = st.text_input("Enter Your Name:")
fname = st.text_input("Enter Your Father Name:")
adr = st.text_area("Enter Your Address:")
classdata = st.selectbox("Enter Your Class :",("BCA","MCA","BA","BBA"))
button = st.button("SUBMIT")
if button:
    st.markdown(f"""  
    Name : {name},
    Father Name : {fname},
    Address : {adr},
    Class : {classdata}""")