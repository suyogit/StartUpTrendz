import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title='StartUp Funding Trendz', page_icon=':moneybag:', layout='wide')

df=pd.read_csv('startup_funding_cleaned.csv')
df['date']=pd.to_datetime(df['date'])
df['month']=df['date'].dt.month
df['year']=df['date'].dt.year
#df['Investors Name']=df['Investors Name'].fillna('Unknown')

#data cleaned on kaggle using below commands

#************************************************************

# # This Python 3 environment comes with many helpful analytics libraries installed
# # It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# # For example, here's several helpful packages to load

# import numpy as np # linear algebra
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# # Input data files are available in the read-only "../input/" directory
# # For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

# import os
# for dirname, _, filenames in os.walk('/kaggle/input'):
#     for filename in filenames:
#         print(os.path.join(dirname, filename))

# # You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# # You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session
# df= pd.read_csv('/kaggle/input/indian-startup-funding/startup_funding.csv')
# df.head(5)
# df.info()
# df.drop(columns=['Remarks'], inplace=True)
# df.head()
# df.set_index('Sr No', inplace=True)
# df.head()
# df.rename(columns={
#     'Date dd/mm/yyyy':'date',
#     'Startup Name':'startup',
#     'Industry Vertical':'vertical',
#     'SubVertical':'subvertical',
#     'City  Location':'city',
#     'Investors Name':'investors',
#     'InvestmentnType':'round',
#     'Amount in USD':'amount'
    
    
# },inplace=True)
# df.info()
# df['amount'].fillna('0')
# df['amount']=df['amount'].str.replace(',','')
# df['amount']=df['amount'].str.replace('undisclosed','0')
# df['amount']=df['amount'].str.replace('unknown','0')
# df['amount']=df['amount'].str.replace('Undisclosed','0')
# df=df[df['amount'].str.isdigit()]
# df['amount']=df['amount'].astype('float')
# df.head()
# def to_rs(dollar):
#     rs= dollar*135
#     return rs/10000000
# df['amount']=df['amount'].apply(to_rs)
# df['amount']
# df['date']

# df['date']= df['date'].str.replace('05/072018','05/07/2018')
# df['date']=pd.to_datetime(df['date'],format='%d/%m/%Y', errors='coerce')
# df['date'].dt.day

# df= df.dropna(subset=['date','startup','vertical','city','investors','round','amount'])
# df
# df.to_csv('startup_funding_cleaned.csv', index=False)


#************************************************************

st.sidebar.title("StartUp Funding Trendz")
option= st.sidebar.selectbox('Select the option',['Overall Analysis','Investors','StartUp Industry'])

def load_overall_analysis():
    st.title('StartUp Funding Analysis')
    st.write('This is the overall analysis of the StartUp Funding')
    #total invested amount
    total= round(df['amount'].sum())
    #max amount of investment
    max_funding=df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
    #average ticket size
    avg_funding= df.groupby('startup')['amount'].sum().mean()
    #total funded startups
    num_startups=df['startup'].nunique()

    col1,col2,col3, col4=st.columns(4)
    with col1:
         st.metric('Total Funding',str(total)+' Cr')
    with col2:
            st.metric('Max Funding',str(max_funding)+' Cr')
    with col3:
            st.metric('Average Funding',str(round(avg_funding))+' Cr')
    with col4:
            st.metric('Total StartUps Funded',num_startups)
    st.header('Month by Month Graph')
    selected_option=st.selectbox('Select Type',['Total','Count'])
    if selected_option=='Total':
          temp_df=df.groupby(['year','month'])['amount'].sum().reset_index()
    else:
           temp_df=df.groupby(['year','month'])['amount'].count().reset_index()
          
          
   
    temp_df['x_axis']=temp_df['month'].astype('str')+ '-'+ temp_df['year'].astype('str')
    fig, ax= plt.subplots()
    ax.plot(temp_df['x_axis'],temp_df['amount'])
    st.pyplot(fig)
    
         


def load_inverstor_details(investor):
    st.title(investor)
    #loading the recent 5 investment of investor
    recent=df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('Recent Investments')
    st.dataframe(recent)
    
   
    col1,col2=st.columns(2)
    with col1:
         #loading the biggest investments of investor
            biggest=df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head().reset_index()
            st.subheader('Biggest Investments')
            #st.dataframe(biggest)
            fig, ax= plt.subplots()
            ax.bar(biggest['startup'],biggest['amount'])
            st.pyplot(fig)
    with col2:
         #pie char of sectors invested in by investor
            sectors=df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum().sort_values(ascending=False)
            st.subheader('Sectors Invested In')
            fig, ax= plt.subplots()
            ax.pie(sectors, labels=sectors.index, autopct='%1.1f%%')
            st.pyplot(fig)

    #plot a liniar graph of inverstment year wise
    df['year']=df['date'].dt.year
    # df.info()
    years= df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum() # it is a series because we are using groupby
    #print(years)
    st.subheader('Investment Year Wise')
    fig2, ax2= plt.subplots()
    #debugging
    # print(years.index)
    # print(years.values)

    ax2.plot(years.index,years.values)
    st.pyplot(fig2)

if option=='Overall Analysis':
    # st.title('StartUp Funding Analysis')
    # st.write('This is the overall analysis of the StartUp Funding')
    # st.write(df)
    load_overall_analysis()

elif option=='Investors':
    selected_investor =st.sidebar.selectbox('Select the option',sorted(set(df['investors'].str.split(',').sum())))
    btn1=st.sidebar.button('Search')
    st.title('Investor Analysis')
    if btn1:
        load_inverstor_details(selected_investor)


else:
    st.sidebar.selectbox('Select the option',sorted(df['startup'].unique().tolist()))
    btn2=st.sidebar.button('Search')
    st.title('StartUp Industry Analysis')