import streamlit as st
from my_mail import send_mail
import pandas

data  = pandas.read_csv("topics.csv")

with st.form(key= "my_forms"):
    user_email = st.text_input(label="Your Email Address")
    
    selected_option = st.selectbox('What topic do you want to discuss ?',data['topic'])
    user_msg = st.text_area("Type Your Message")
    message = f"""\
Subject : New Email From{user_email}

from{user_email}
{selected_option}
{user_msg}
    
    
    
    """
    button = st.form_submit_button("submit")
    if button:
       send_mail(message)
       st.info("Your email was sent Successfully")  

