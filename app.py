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

#st.header('Input Parameters')


# num1 = st.number_input("Enter first number: ")
# num2 = st.number_input("Enter second number: ")
# num3 = st.number_input("Enter third number: ")
 
# code = '''(if (num1 > num2) and (num1 > num3):)
#   largest = num1
# elif (num2 > num1) and (num2 > num3):
#   largest = num2
# else:
#   largest = num3
#  print("The largest number is",largest)
# '''
#st.code(code, language='python')
# if (num1 > num2) and (num1 > num3):
#   st.largest = num1
# elif (num2 > num1) and (num2 > num3):
#   st.largest = num2
# else:
#   st.largest = num3
# print("The largest number is",st.largest)

st.header('Enter Three Numbers')

def user_input_features():
    
    number_1 = st.number_input("number_1")
    number_2 = st.number_input("number_2")
    number_3 = st.number_input("number_3")
    

    data = {'NUMBER_1': number_1,
            'NUMBER_2': number_2,
            'NUMBER_3': number_3
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df.to_dict())



largest=df.max()
st.subheader('Largest Number')
st.write(largest)


