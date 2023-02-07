import streamlit as st
import pandas


st.set_page_config(layout="wide")


st.header("The Best Company")

content = """
ctetur iure tempora, voluptas ipsa vero perspiciatis provident velit fugiat, atque ipsum.
Laboriosam eum inventore officia nulla molestias? Dolor rem voluptatem, veritatis pariatur iste omnis sapiente at temporibus minima esse totam laboriosam minus, incidunt obcaecati harum et aut eius qui repudiandae facere?
Eius ipsam recusandae voluptatem magni ate.

"""
st.write(content)

st.subheader("Our Team")

col1,empty_col,col2,empty_col,col3 = st.columns([1.5,0.5,1.5,0.5,1.5])

data = pandas.read_csv("data.csv",sep=",")

with col1:
    for index,row in data[0:4].iterrows():
        st.subheader(row['first name'].capitalize()+' '+row['last name'].capitalize())
        st.write(row["role"])
        st.image("images/"+row["image"])


with col2:
    for index,row in data[4:8].iterrows():
        st.subheader(row['first name'].capitalize()+' '+row['last name'].capitalize())
        st.write(row["role"])
        st.image("images/"+row["image"])


with col3:
    for index,row in data[8:].iterrows():
        st.subheader(row['first name'].capitalize()+' '+row['last name'].capitalize())
        st.write(row["role"])
        st.image("images/"+row["image"])


