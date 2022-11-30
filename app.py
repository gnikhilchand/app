import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle

st.header("""
# Finding largest among 3 given numbers
This app predicts the largest among 3 given numbers
""")
# #Get Input

# st.header('Enter Three Numbers')

# def user_input_features():
    
#     number_1 = st.number_input("number_1")
#     number_2 = st.number_input("number_2")
#     number_3 = st.number_input("number_3")
    

#     data = {'NUMBER_1': number_1,
#             'NUMBER_2': number_2,
#             'NUMBER_3': number_3
#             }
#     features = pd.DataFrame(data, index=[0])
#     return features

# df = user_input_features()

# st.subheader('User Input parameters')
# st.write(df.to_dict())



# largest=df.max()
# st.subheader('Largest Number')
# st.write(largest)
title = "Largest Number Among 3"

st.set_page_config(page_title=title)

st.title('Largest Number Finder')

x = st.number_input('Enter first number')
y = st.number_input('Enter second number')
z = st.number_input('Enter third number')

l=[x,y,z]
if x == y == z:
  st.write("The numbers are Equal")
else:
  st.write(max(l),"is the largest number")


