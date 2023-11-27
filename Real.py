import streamlit as st
import joblib

st.header("This Is A Model Give The Following Inputs: ")

gender=st.radio("Select Your Gender: ",['Male','Female'],horizontal=True)

if gender=='Male':
    Gender_val = 1
else:
    Gender_val = 0

age = st.slider("Select your age")

cigyes = st.radio("DO You Smoke Ciggarattes: ",['Yes','No'],horizontal=True)

if cigyes=='Yes':
    cigyn = 1
else:
    cigyn = 0

cig = st.number_input("Enter Number Of Ciggarettes You Consume In A Day:")

bmi = st.number_input("Enter Your BMI:")

if st.button("Predict"):
    heart_disease_model = joblib.load("HeartDiseaseMDL.h5")
    prediction = heart_disease_model.predict([[Gender_val,age,cigyn,cig,bmi]])
    st.text("Based on the inputs you provided")
    st.success(prediction[0])
