# from predict import predict, get_user_options, get_signal_for_plotting, get_vibration_dataframe

import streamlit as st
import matplotlib.pyplot as plt
import requests
import pandas as pd
import plotly.graph_objects as go
import numpy as np


ANIMATION_STEP = 24
NORMAL_COLOR = 'lightcyan'
WARNING_COLOR = 'lightsalmon'
FAILPOINT = 550

def create_mean_vibration_animation(failpoint = None):

    # df = get_vibration_dataframe()
    df  = requests.get('http://service1:3011/get_vibration_dataframe').json()["results"]["df"]
    df = pd.DataFrame(df )

    fig = go.Figure(
    data=[go.Scatter(x=np.arange(len(df.index[:ANIMATION_STEP])), y=df.iloc[:ANIMATION_STEP,0]),
          go.Scatter(x=np.arange(len(df.index[:ANIMATION_STEP])), y=df.iloc[:ANIMATION_STEP,1]),
          go.Scatter(x=np.arange(len(df.index[:ANIMATION_STEP])), y=df.iloc[:ANIMATION_STEP,2]),
          go.Scatter(x=np.arange(len(df.index[:ANIMATION_STEP])), y=df.iloc[:ANIMATION_STEP,3])
         ],
    layout=go.Layout(
        xaxis=dict(range=[0, len(df)], autorange=False),
        yaxis=dict(range=[0, 0.2], autorange=False),
        #title="Start Title",
        plot_bgcolor = NORMAL_COLOR,
        updatemenus=[dict(
            type="buttons",
            buttons=[dict(label="Play",
                            # color= "black",
                          method="animate",
                          args=[None])])]
    ),

    frames=[go.Frame( data=[go.Scatter(x=np.arange(len(df.index[:i*ANIMATION_STEP])), y=df.iloc[:i*ANIMATION_STEP,0]),
                            go.Scatter(x=np.arange(len(df.index[:i*ANIMATION_STEP])), y=df.iloc[:i*ANIMATION_STEP,1]),
                            go.Scatter(x=np.arange(len(df.index[:i*ANIMATION_STEP])), y=df.iloc[:i*ANIMATION_STEP,2]),
                            go.Scatter(x=np.arange(len(df.index[:i*ANIMATION_STEP])), y=df.iloc[:i*ANIMATION_STEP,3])
                           ],layout=go.Layout(plot_bgcolor = (WARNING_COLOR if (failpoint and failpoint <= i*ANIMATION_STEP) else NORMAL_COLOR))
                    ) for i in range(len(df)//ANIMATION_STEP + 2 ) ]
    )
    return fig


st.title('Anomaly Detection for Predictive Maintenance of Bearings')

user_options  = requests.get('http://service1:3011/user_op').json()["results"]["op"]

# user_options = get_user_options()
if  user_options : 
    option = st.selectbox(
        "Select a vibration snapshot to be analyzed!",
        user_options)

    if st.button("Check for anomaly!"):
        if not option:
            st.warning("No timestamp selected!")
        else:
            signal  = requests.get('http://service1:3011/b_pricit' , params= {"option":option}).json()["results"]["op"]
            if (bool (signal)):
                st.error('Maintenance needed!')
            else:
                st.success("Vibrations look normal. Carry on!")

    if st.button("Show Signal!"):
        if not option:
            st.warning("No timestamp selected!")
        else:

            signal  = requests.get('http://service1:3011/user_opselect' , params= {"option":option}).json()["results"]["op"][0]
            
            # signal = get_signal_for_plotting(option)
            signal = np.array(signal)
            fig, ax = plt.subplots()
            ax.plot(signal.transpose())
            st.pyplot(fig)

    if st.button("Plot averaged vibrations!"):
        fig = create_mean_vibration_animation()
        st.plotly_chart(fig)

    if st.button("Monitor vibrations!"):
        fig = create_mean_vibration_animation(failpoint=FAILPOINT)
        st.plotly_chart(fig)

