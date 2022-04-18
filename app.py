import streamlit as st
import pandas as pd
import helper


st.sidebar.title("Company Data")

df=pd.read_csv("D:\Project Data\Web scrapping project\comp_info_3.csv")

selected_comp = st.sidebar.selectbox(
    'How would you like to be contacted?',
     df['name'].values)

if st.sidebar.button("Show"):
    a= helper.fetch_stats(selected_comp,df)
    st.write('Name : ',a.iat[0,1])
    st.write('Rating : ',a.iat[0,2])
    st.write('Review : ',a.iat[0,3])
    st.write('company_type : ',a.iat[0,4])
    st.write('Head_Quarters : ',a.iat[0,5])
    st.write('Company_Age :' ,a.iat[0,6])
    st.write('No_of_Employee : ',a.iat[0,7])
    st.write('About : ',a.iat[0,8])

    
