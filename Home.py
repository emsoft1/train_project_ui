import streamlit as st
# from .pages import Home as homepage
# import pages.prediction as pri

import pages.images as imgpage
import datetime
import requests
import matplotlib.pyplot as plt
import numpy as np
test_name= ""
st.write("home some text over project ")
list  = requests.get('http://service1:3011/test_list').json()["results"]
for test in list :
    if st.button(test):
        test_name= test
if test_name != "":
    parm = {"test_name":test_name}
    data = requests.get('http://service1:3011/predict' ,params=parm).json()

    if data["results"]["warning"] ==True:
        new_title = f'<p style="font-family:sans-serif; color:red; font-size: 42px;">this bearing go to fail </p>'
        st.markdown(new_title, unsafe_allow_html=True)
    else :
        new_title = f'<p style="font-family:sans-serif; color:Green; font-size: 42px;">this bearing is ok </p>'
        st.markdown(new_title, unsafe_allow_html=True)
    fig, ax = plt.subplots()
    ax.plot( data["results"]["vib"])
    st.pyplot(fig)
