import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from plotly import graph_objs as go 
from sklearn.linear_model import LinearRegression
import numpy as np
import pickle

st.set_option('deprecation.showPyplotGlobalUse',False)

data=pd.read_csv("Salary_Data.csv")
x=np.array(data['YearsExperience']).reshape(-1,1)
lr=LinearRegression()
lr.fit(x,np.array(data['Salary']))


st.title("Salary Predictor")
st.image("https://tse1.mm.bing.net/th?id=OIP.rm55EZ0dmsdvQjq_iCiu3AHaDt&pid=Api&P=0&h=180",width=800)
nav=st.sidebar.radio("Navigation",["Home","Predictor","Dashboard","Contribute"])
if nav=="Home":

    if st.checkbox("Show Table"):
        st.table(data)

    graph=st.selectbox("What kind of graph ?",["Non-Interactive","Interactive"])
    
    val=st.slider("Filter data using years",0.20)
    data=data.loc[data["YearsExperience"]>=val]
    if graph=="Non-Interactive":
        plt.figure(figsize=(10,5))
        plt.scatter(data["YearsExperience"],data["Salary"])
        plt.ylim(0)
        plt.ylabel("YearsExperience")
        plt.xlabel("Salary")
        plt.tight_layout()
        st.pyplot()
    if graph=="Interactive":
        layout=go.Layout(
            xaxis=dict(range=[0,16]),
            yaxis=dict(range=[0,210000])
        )
        fig=go.Figure(data=go.Scatter(x=data["YearsExperience"],y=data["Salary"]))
        st.plotly_chart(fig)

if nav=="Predictor":
    st.header("Know your Salary")
    val=st.number_input("Enter you exp",0.00,20.00,step=0.25)
    val=np.array(val).reshape(1,-1)
    #model_load=pickle.load(open('model.xyz','rb'))
    pred=lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your predicted salary is{round(pred)} rupees per month")

if nav=="Contribute":
    st.header("Contribute to our dataset")
    ex=st.number_input("Enter you exp",0.00,20.00,step=0.25)
    sal=st.number_input("Enter our salary",0.00,100000.00,step=1000.00)
    if st.button("submit"):
        to_add={"YearsExperience":[ex],"Salary":[sal]}
        to_add=pd.DataFrame(to_add)
        to_add.to_csv("Salary_Data.csv",mode='a')
        st.success("Submitted")

if nav=="Dashboard":
    plt.style.use('dark_background')
    marks=[90,34,56,72,64,30]
    names=["praveen","sunny","saketh","raju","ashish","nikhil"]


    ice_creams=[30,12,23,21,4,10]
    names1=["mango","chacobar","pine apple","mango","vanillia","choclate"]

    fig=plt.figure()
    plt.bar(names,marks,color="green",width=0.5)

    fig2=plt.figure()
    plt.pie(ice_creams,labels=names1)


    c1,c2=st.columns(2)
    c1.pyplot(fig2)
    c2.pyplot(fig)
