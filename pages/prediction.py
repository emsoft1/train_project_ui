import streamlit as st
# from .pages import Home as homepage
# import pages.prediction as pri


import datetime
import requests
import matplotlib.pyplot as plt
import numpy as np
st.write("pridiction is running  is ruunnig ")
speed = st.slider('Train speed', min_value=35, max_value=50)
faul_type = st.selectbox(
    ' what is the type of fault :',
    ('None', 'crack'))

fault_severity = st.slider('Fault Distance',min_value=200, max_value=999)
fault_dis = st.slider('Fault severity ', 1, 5, 1)

if st.button('Predict'):
    parm = {"speed":speed ,"pos" :fault_dis , "sev":fault_severity , "types":faul_type}
    # data = requests.get('http://service1:3011/train_prob' ,params=parm).json()
    # st.write(data["results"]["data"])
    container = st.container(border=True)
    container.write(f"This is you prediction")

    # if data["results"]["data"]["good"]["0"] ==False :
    # f_t=str( data["results"]["data"]["good"]["0"])
    # f_s=str( data["results"]["data"]["fail"]["0"][0])
    # f_d=str( data["results"]["data"]["fail"]["0"][1])
    # st.write("ruuning :!!!!")
    container.write(f"Fault type is : Crack ")
    container.write(f"Fault severity is : 4.2 ")
    container.write(f"Fault distance : 505 ")
