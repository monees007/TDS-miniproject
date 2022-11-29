import streamlit as st
st.header('ODD or EVEN')

number = st.number_input('Enter number to proceed')
if number%2:
  res='EVEN'
else:
  res='ODD'
  
st.write(res)

