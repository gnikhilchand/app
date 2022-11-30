import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.write("""
# Finding largest among 3 given numbers
This app predicts the largest among 3 given numbers
""")
#Get Input

st.header('User Input Parameters')

def maximum(a, b, c): 
   list = [a, b, c] 
   return max(list) 
# Driven code  
x = st.number_input("Enter First number"))
y = st.number_input("Enter Second number"))
z = st.number_input("Enter Third number"))
print("Maximum Number is ::>",maximum(x, y, z)) 


