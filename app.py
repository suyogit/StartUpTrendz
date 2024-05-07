import streamlit as st
import pandas as pd
import numpy as np

df=pd.read_csv('startup_funding_cleaned.csv')
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

if option=='Overall Analysis':
    st.title('StartUp Funding Analysis')
    st.write('This is the overall analysis of the StartUp Funding')
    st.write(df)

elif option=='Investors':
    st.sidebar.selectbox('Select the option',sorted(set(df['investors'].str.split(',').sum())))
    btn1=st.sidebar.button('Search')
    st.title('StartUp Funding Analysis')

else:
    st.sidebar.selectbox('Select the option',sorted(df['startup'].unique().tolist()))
    btn2=st.sidebar.button('Search')
    st.title('StartUp Industry Analysis')