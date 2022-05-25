import streamlit as st
import requests
import pandas as pd
import json

# lien à faire avec FastAPI
# http://127.0.0.1:8000 is endpoint from fastapi
#response = requests.post("http://127.0.0.1:8000/predict")
#st.write(response)


st.title('Is this company likely to fail ?')

with st.form("input_form"):
    st.write("Select values for features")
    dettes = st.slider("Form slider")
    statut = st.selectbox(
        'Quel statut ?', 
        ('Société à responsabilité limitée (SARL)', 'Société par actions simplifiée', "Société anonyme à conseil d'administration", "Entrepreneur individuel"))
    ape = st.selectbox(
        'Quel secteur ?', 
        ('A', 'B', 'C', 'D', 'E' 'F', 'G'))

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        test={"dettes":'2',"statut":'Société par actions simplifiée',"ape":'A'}
        payload = {"dettes":dettes,"statut":statut,"ape":ape}
        test2 = json.dumps(payload)
        #https://appdividend.com/2022/03/20/python-requests-post/
        #headers={'Content-Type':'application/json'}, 
        response = requests.post("http://127.0.0.1:8000/predict", headers={'Content-Type':'application/json'}, data=json.loads(test2))
        st.write(response.json())
        st.write(type(test2))
        st.write(test2)




# à l'interieur du formulaire
with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")
    option = st.selectbox(
        'How would you like to be contacted?', 
        ('Email', 'Home phone', 'Mobile phone'))


    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val, "selectbox", option)

st.write("Outside the form")

