import streamlit as st
import random
import pages.images as imgpage
import datetime
import requests
import matplotlib.pyplot as plt
import numpy as np



img_list  = requests.get('http://service1:3011/img_list').json()["results"]
# st.write(img_list)
filename= ""
types = ""
for test in img_list :
    if st.button(f"Select a Random {test} image"):
        filename= random.choice(img_list[test])
        types=test

if filename != "":
    st.image(f"https://train_api.overhaul-solutions.com/{types}/{filename}" ,  width=600)
    parm = {"cat":types, "filename":filename}
    data = requests.get('http://service1:3011/img_pridiction' ,params=parm).json()
    # st.write(data)
    if data["results"]["lable"] =="fail":
        new_title = f'<p style="font-family:sans-serif; color:red; font-size: 42px;">this bearing go to fail with probability Of {float(data["results"]["probability"]) * 100}  </p>'
        st.markdown(new_title, unsafe_allow_html=True)
    else :
        new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 42px;">this bearing is ok with probability Of {float(data["results"]["probability"]) * 100}   </p>'
        st.markdown(new_title, unsafe_allow_html=True)
    # fig, ax = plt.subplots()
    # ax.plot( data["results"]["vib"])
    # st.pyplot(fig)