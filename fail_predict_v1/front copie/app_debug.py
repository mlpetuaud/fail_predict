
import requests
import pandas as pd
import json

import streamlit as st
#import streamlit_authenticator as stauth

import users

# lien à faire avec FastAPI
# http://127.0.0.1:8000 is endpoint from fastapi
#response = requests.post("http://127.0.0.1:8000/predict")
#st.write(response)



header_section = st.container()
main_section = st.container()
login_section = st.expander("LOG IN")
logout_section = st.container()
signup_section = st.expander("SIGN UP")

def show_prediction_page():
    with st.form("input_form"):
        st.title('Is this company likely to fail ?')
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
            test={
    "dettes": 3000,
    "statut": "Société par actions simplifiée",
    "APE": "C"
    }
            #test={"dettes":2,"statut":'Société par actions simplifiée',"ape":'A'}
            payload = {"dettes":dettes,"statut":statut,"APE":ape}
            test2 = json.dumps(payload)
            dataform = str(test2).strip("'<>() ").replace('\'', '\"')
            headers = {"Content-Type": "application/json", "Accept": "application/json"}
            #https://appdividend.com/2022/03/20/python-requests-post/
            #headers={'Content-Type':'application/json'}, 
            response = requests.post("http://127.0.0.1:8000/predict", headers=headers, json=payload)
            st.write(response.json())
            st.write(type(test2))
            st.write(test2)


def show_main_page():
    with main_section:
        st.text("Welcome to the main section")
        do_clicked = st.button("Do something", key="do")
        if do_clicked:
            st.balloons()

def logged_out_clicked():
    st.session_state['logged_in'] = False

def show_logout_page():
    login_section.empty()
    with logout_section:
        st.button("Log Out", key="logout", on_click=logged_out_clicked)

def logged_in_clicked(username, password):
    st.success(f"Logged In as {username}, {password}")
    st.session_state['logged_in'] = True
    # if login(username, password):
    #     st.session_state['logged_in'] = True
    # else:
    #     st.session_state['logged_in'] = False
    #     st.error("Invalid user name or password")

def signup_clcked(username, password):
    st.success("You have successfully created your account")
    # INSERT values to DB
    # login (session_state = True)
    pass

def show_login_page():
    with login_section:
        if st.session_state['logged_in'] == False:
            username_login = st.text_input("User Name", key="user_login", value="")
            password_login = st.text_input("Choose a password", type="password", value="")
            st.button("Login", on_click=logged_in_clicked, args= (username_login, password_login))

def show_signup_page():
    with signup_section:
        if st.session_state['logged_in'] == False:
            username_signup = st.text_input("User Name", key="user_signup", value="")
            password_signup = st.text_input("Password", type="password", value="")
            st.button("SIGN UP", on_click=signup_clcked, args=(username_signup, password_signup))
            #st.button("Login", on_click=logged_in_clicked, args= (username, password))      


def show_authentification_page():
    with login_section:
        if st.session_state['logged_in'] == False:
            st.subheader("Login section")
            username_login = st.text_input("User Name", key="user_login", value="")
            password_login = st.text_input("Choose a password", type="password", value="")
            st.button("Login", on_click=logged_in_clicked, args= (username_login, password_login))
    with signup_section:
        if st.session_state['logged_in'] == False:
            st.subheader("Create a new account")
            username_signup = st.text_input("User Name", key="user_signup", value="")
            password_signup = st.text_input("Password", type="password", value="")
            st.button("Sign Up", on_click=signup_clcked, args=(username_signup, password_signup))

with header_section:
    st.title("Welcome to the Streamlit App")
    # first run will have nothing in session state - initialization of session_state
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
        print("1")
        print(st.session_state['logged_in'])
        #show_authentification_page()
        # col1, col2 = st.columns(2)
        # with col1:
        # show_login_page()
        # with col2:
        # show_signup_page()
    else:
        if st.session_state['logged_in']:
            print("2")
            # show_logout_page()
            # show_prediction_page()
            # show_main_page()
        else:
            print("3")
            # show_authentification_page()

# ---- API CONNECTION & FORM ----







# à l'interieur du formulaire
# with st.form("my_form"):
#     st.write("Inside the form")
#     slider_val = st.slider("Form slider")
#     checkbox_val = st.checkbox("Form checkbox")
#     option = st.selectbox(
#         'How would you like to be contacted?', 
#         ('Email', 'Home phone', 'Mobile phone'))


#     # Every form must have a submit button.
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         st.write("slider", slider_val, "checkbox", checkbox_val, "selectbox", option)

# st.write("Outside the form")

