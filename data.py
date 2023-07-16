import streamlit as st
import numpy as np
import pandas as pd
import time

a=[1,2,3,4,5,6,7,8]
n=np.array(a)
S=n.reshape((2,4))

dic = {
    "name":["praveen","sunny"],
    "age":[21,32],
    "city":["hyd","delhi"]
}

data = pd.read_csv("Salary_Data.csv")

st.dataframe(data,width=500,height=500)
st.table(data)
st.table(dic)
st.json(dic)
st.write(dic)

@st.cache
def ret_time(a):
    time.sleep(a)
    return time.time()
x = st.checkbox("terms & conditions")

st.write(x)

if x:
    st.write("well done you have checked")
else:
    st.write("please check the checkbox")

if st.checkbox("1"):
    st.write(ret_time(1))

if st.checkbox("2"):
    st.write(ret_time(2))
