import pickle
import pandas as pd
import streamlit as st


#load the data
df = pd.read_csv("cleaned_df.csv")


#load the pre trained model
with open("Log_reg_model.pkl","rb") as file:
    model = pickle.load(file)


#page setup
st.set_page_config(page_icon="🌐",page_title="Telco-Customer-Churn",layout="wide")

with st.sidebar:
    st.title("Telco Customer Churn Predictor")

    st.image("customer.jfif")


#user input
#['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
       #'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
       #'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
       #'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
       #'MonthlyCharges', 'TotalCharges']

col1,col2, col3 = st.columns(3)

with col1:
    
    gender = st.radio("Gender: ",options=["Male","Female"],horizontal=True)
    gender = 1 if gender=="Male" else 0

    SeniorCitizen = st.radio("Senior Citizen: ",options=["Yes","No"],horizontal=True)
    SeniorCitizen = 1 if SeniorCitizen=="Yes" else 0

    Partner = st.radio("Partner: ",options=["Yes","No"],horizontal=True)
    Partner = 1 if Partner=="Yes" else 0

    Dependents = st.radio("Dependents: ",options=["Yes","No"],horizontal=True)
    Dependents = 1 if Dependents=="Yes" else 0

    Tenure = st.number_input("Tenure in Months: ",min_value=0,max_value=72)

    PhoneService = st.radio("Phone Service: ",options=["Yes","No"],horizontal=True)
    PhoneService = 1 if PhoneService=="Yes" else 0

    d= {"Yes":2,"No":0, "No phone service":1}
    MultipleLines = st.selectbox("Multiple Lines: ",options=d)
    MultipleLines = d[MultipleLines]

with col2:

    dic= {"No":2,"DSL":0, "Fiber Optic":1}
    InternetService = st.selectbox("Internet Service: ",options=dic)
    InternetService = dic[InternetService]

    d1= {"Yes":2,"No":0, "No Internet service":1}
    OnlineSecurity = st.selectbox("Online Security: ",options=d1)
    OnlineSecurity = d1[OnlineSecurity]

    d2= {"Yes":2,"No":0, "No Internet service":1}
    OnlineBackup = st.selectbox("Online Backup: ",options=d2)
    OnlineBackup = d2[OnlineBackup]

    d3= {"Yes":2,"No":0, "No Internet service":1}
    DeviceProtection = st.selectbox("Device Protection: ",options=d3)
    DeviceProtection = d3[DeviceProtection]

    d4= {"Yes":2,"No":0, "No Internet service":1}
    TechSupport = st.selectbox("Tech Support: ",options=d4)
    TechSupport = d4[TechSupport]

    d5= {"Yes":2,"No":0, "No Internet service":1}
    StreamingTV = st.selectbox("Streaming TV: ",options=d5)
    StreamingTV = d5[StreamingTV]      
    
       
   
with col3:
    d6= {"Yes":2,"No":0, "No Internet service":1}
    StreamingMovies = st.selectbox("Streaming Movies: ",options=d6)
    StreamingMovies = d6[StreamingMovies]

    d7= {"Month-to-month":0,"One year":1, "Two year":2}
    Contract = st.selectbox("Contract: ",options=d7)
    Contract = d7[Contract]

    PaperlessBilling = st.radio("Paperless Billing: ",options=["Yes","No"],horizontal=True)
    PaperlessBilling = 1 if PaperlessBilling=="Yes" else 0  
    
    
    d8= {"Electronic check":2,"Mailed check":3, "Bank transfer (automatic)":0,"Credit card (automatic)":1}
    PaymentMethod = st.selectbox("Payment Method: ",options=d8)
    PaymentMethod = d8[PaymentMethod]


    MonthlyCharges = st.number_input("Monthly Charges: ",min_value=0.0)
    TotalCharges = st.number_input("Total Charges: ",min_value=0.0)

    
    
    if col2.button("Predict"):
        #data = [[gender,SeniorCitizen,Partner,Dependents,Tenure,PhoneService, MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV, StreamingMovies, Contract, PaperlessBilling,PaymentMethod, MonthlyCharges, TotalCharges]]
        data = pd.DataFrame([[gender,SeniorCitizen,Partner,Dependents,Tenure,PhoneService, MultipleLines,InternetService,OnlineSecurity,OnlineBackup,DeviceProtection,TechSupport,StreamingTV, StreamingMovies, Contract, PaperlessBilling,PaymentMethod, MonthlyCharges, TotalCharges]], columns=model.feature_names_in_)


        pred = model.predict(data)[0]
        if pred==0:
            st.subheader("The customer is not likely to churn.")
        else:
            st.subheader("The customer is likely to churn.") 