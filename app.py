import streamlit as st
import pandas as pd
import numpy as np

df=pd.read_csv('startup_funding.csv')
df['Investors Name']=df['Investors Name'].fillna('Unknown')

st.sidebar.title("StartUp Funding Trendz")
option= st.sidebar.selectbox('Select the option',['Overall Analysis','Investors','StartUp Industry'])

if option=='Overall Analysis':
    st.title('StartUp Funding Analysis')
    st.write('This is the overall analysis of the StartUp Funding')
    st.write(df)

elif option=='Investors':
    st.sidebar.selectbox('Select the option',sorted(df['Investors Name'].unique().tolist()))
    btn1=st.sidebar.button('Search')
    st.title('StartUp Funding Analysis')

else:
    st.sidebar.selectbox('Select the option',sorted(df['Startup Name'].unique().tolist()))
    btn2=st.sidebar.button('Search')
    st.title('StartUp Industry Analysis')