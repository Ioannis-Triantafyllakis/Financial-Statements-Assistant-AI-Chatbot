import streamlit as st

st.title('Test')
st.write('Test')

with open('./media/styles.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)