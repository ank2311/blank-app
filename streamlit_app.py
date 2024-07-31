import streamlit as st
import pandas as pd

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

form = st.form(key='my-form')
name = form.text_input('Enter your name')
submit = form.form_submit_button('Submit')

st.write('Press submit to have your name printed below')

if submit:
    st.write(f'hello {name}')


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
   #read xls or xlsx
    df1=pd.read_excel(uploaded_file);
    st.write(df1)
