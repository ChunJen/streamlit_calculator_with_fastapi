import streamlit as st
import json
import requests

st.title("Basic Calculator 🧮")

option = st.selectbox('What operation would you like to do?',
                      ('Addition', 'Subtraction', 'Multiplication', 'Division'))

st.write(f"You selected {option}!")
st.write("Enter two numbers to perform the operation")
x = st.number_input("Enter the first number")
y = st.number_input("Enter the second number")

inputs = {'operation': option, 'x': x, 'y': y}

if st.button('Calculate'):
    response = requests.post(url = "http://127.0.0.1:8000/calculate/", 
                             data = json.dumps(inputs))
    st.subheader(f"The result from fastAPI🚀 is {response.json()}")