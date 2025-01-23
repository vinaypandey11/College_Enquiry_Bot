import streamlit as st
import os

# Dictionary to store username and password
credentials = {
    "vinay": "VINA2002",
    "prachi": "PRAC2003",
    "akshay": "AKSH2003",
    "sayali": "SAYA2003",
    "aishwarya": "AISH2003",
    "pranita": "PRAN2003"
}

# Function to display the login page
def login():
    st.title("Login Page")
    
    # Input fields for username and password
    username = st.text_input("Enter your username:")
    password = st.text_input("Enter your password:", type='password')

    # Login button
    if st.button("Login"):
        # Check if the credentials match
        if username in credentials and credentials[username] == password:
            # Store username in session state
            st.session_state["logged_in_user"] = username
            st.success(f"Welcome, {username}!")

            # Redirect to the chatbot page
            st.write("Redirecting to chatbot...")
            st.rerun()
        else:
            st.error("Invalid username or password. Please try again.")

# Main logic for navigation
if "logged_in_user" not in st.session_state:
    login()
else:
    # Automatically navigate to the chatbot if the user is logged in
    #st.write(f"Redirecting to chatbot for {st.session_state['logged_in_user']}...")
    with open("C:\\Users\\DELL\\OneDrive\\Desktop\\Clients\\A2- Akshay\\code\\chatbot.py") as f:  # Ensure this path is correct
        exec(f.read())
