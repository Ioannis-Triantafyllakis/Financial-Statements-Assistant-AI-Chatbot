import streamlit as st

with open('./media/styles.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

st.title('Test title')
st.write('Test text')

