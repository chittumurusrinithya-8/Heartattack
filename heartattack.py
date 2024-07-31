import streamlit as st

import pickle

trained_model = pickle.load(open('trained_model.sav','rb'))

# Title
st.title("Heart Attack Precdictor")
age = st.text_input("Enter Your age", "0")
gender = st.selectbox("Gender: ",
                     ['Male', 'Female'])
if gender == 'Male':
    gender = 0
else:
    gender = 1
chp = {"Typical Angina":0,"Atypical Angina":1,"Non-anginal Pain":2,"Asymptomatic":3}
chestpain = st.selectbox("Chest pain type:",["Typical Angina","Atypical Angina","Non-anginal Pain","Asymptomatic"])
chestpain = chp[chestpain]
trestbps = st.text_input("Enter your Resting blood pressure (in mm Hg)","0")
chol = st.text_input("Enter your  Cholestoral in mg/dl fetched via BMI sensor","0")
fbs = st.selectbox("fasting blood sugar:",['True','False'])
if fbs == "True":
    fbs = 1
else:
    fbs = 0
ecgd = {"Normal":0,"ST-T wave normality":1,"Left ventricular hypertrophy":2}
restecg = st.selectbox("Ecg Result:",['Normal','ST-T wave normality','Left ventricular hypertrophy'])
restecg = ecgd[restecg]
thalach =st.text_input("Maximum heart rate achieved","0")
oldpeak = st.text_input("Old peak value calculated from ecg")
slope = st.text_input("slope value calculated from ecg")
thall = st.selectbox("Thalium Stress Test result:",['0','1','2','3'])
exng = st.selectbox("Exercise induced angina:",['Yes','No'])
if exng == "Yes":
    exng = 1
else:
    exng = 0
caa = st.selectbox("number of major vessels:",['0','1','2','3'])


if st.button('Heart Disease Test Result'):

    user_input = [age,gender,chestpain,trestbps,chol,fbs,restecg,thalach,oldpeak,slope,thall,exng,caa]

    user_input = [float(x) for x in user_input]

    heart_prediction = trained_model.predict([user_input])

    if heart_prediction[0] == 1:
        heart_diagnosis = 'The person is having heart disease'
    else:
        heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)


