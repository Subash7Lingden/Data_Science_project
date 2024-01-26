import streamlit as st 
import pickle
import numpy as np 
import pandas as pd 


#import the model
lr = pickle.load(open('lr.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("sales based on ads")



# Advertisement revenue
TV= st.selectbox('TV_ads_revenue',df['TV'])
radio = st.selectbox('Radio_ads_revenue', df['radio'])
newspaper = st.selectbox('Newspaper_ads_revenue',df['newspaper'])

if st.button("submit"):
    #query
    query = np.array([TV, radio, newspaper])
    query =query.reshape(1,3)
    st.title(lr.predict(query))
   





