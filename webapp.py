import pandas as pd
import streamlit as st

heading=st.container()

dataset=st.container()


with heading:
    st.title("welocme to all")
    st.markdown("we will help you filter the data to find insight")
with dataset:
    st.header("please choose one location")
    data=pd.read_csv("samplepython.csv")
    a=st.slider("what is the range",min_value=200000,max_value=900000,value=300000,step=100000)
    datanew=data[data["Impressions"]>=a]
    b=st.text_input("what do u want group","Date")
    datanew1=datanew.groupby(b)['Impressions'].sum()
    datanew1=datanew1.to_frame(name="Total impressions")
    c=st.selectbox("chose number ofrow we want",options=[5,6,7],index=0)
    st.bar_chart(datanew1)
    st.write(datanew1.head(n=7))