import streamlit as st

st.write("pridiction is running  is ruunnig ")
weight = st.slider('Train Weight', 2000, 10000, 200)
speed = st.slider('Train speed', 30, 50, 2)
faul_type = st.selectbox(
    ' what is the type of fault :',
    ('None', 'Crack'))
fault_severity = st.slider('Fault Distance', 10, 990, 20)
fault_dis = st.slider('Fault severity ', 1, 5, 1)

if st.button('Predict'):
    container = st.container(border=True)
    container.write(f"This is you prediction")
    container.write(f"Fault type is :{faul_type} ")
    container.write(f"Fault severity is :{fault_severity}")
    container.write(f"Fault distance : {fault_dis} ")
