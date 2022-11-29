import streamlit as st
st.header('ODD or EVEN')

number = st.number_input('Enter number to proceed')

if st.button("Check"):
  if number%2:
    res='EVEN'
  else:
    res='ODD'

  st.write(res)
else:
  if number%2:
    res='EVEN'
  else:
    res='ODD'
