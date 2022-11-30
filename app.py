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

st.header('Input Parameters')

def user_input_features():
 num1 = st.number_input("Enter first number: ")
 num2 = st.number_input("Enter second number: ")
 num3 = st.number_input("Enter third number: ")
 
 
 if (num1 > num2) and (num1 > num3):
  largest = num1
 elif (num2 > num1) and (num2 > num3):
  largest = num2
 else:
  largest = num3
  return("The largest number is",largest)


