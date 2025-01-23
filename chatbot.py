import streamlit as st
from datetime import datetime
import random
import base64
from streamlit_chat import message

# Function to get greeting based on current time
def get_greeting():
    current_time = datetime.now().time()
    if current_time.hour < 12:
        return "Good Morning"
    elif 12 <= current_time.hour < 17:
        return "Good Afternoon"
    elif 17 <= current_time.hour < 20:
        return "Good Evening"
    else:
        return "Good Night"

# Function to understand user query and generate responses
def response_generator(user_input):
    # Tokenize the input
    tokens = user_input.lower().split()

    # Check if user asked about "subjects" first
    if "subjects" in tokens:
        st.session_state.subjects_requested = True  # Set flag to indicate subjects were requested
        return "_Please select your year:_\n1. _First Year_\n2. _Second Year_\n3. _Third Year_\n4. _Fourth Year_"

    # If user responds with a year, check if they previously asked for subjects
    if st.session_state.get("subjects_requested", False):
        if "first year" in user_input.lower():
            st.session_state.subjects_requested = False  # Reset after responding
            return ("_Following are your subjects for Semester 1:_\n\n"
                    "- _Engineering Physics_\n"
                    "- _Engineering Chemistry_\n"
                    "- _Engineering Mechanics_\n"
                    "- _Engineering Mathematics I_\n"
                    "- _Basic Electrical Engineering_\n"
                    "- _Basic Electronics Engineering_\n"
                    "- _Programming and Problem Solving_\n"
                    "- _Systems in Mechanical Engineering_\n\n"
                    "_Semester 2:_\n\n"
                    "- _Engineering Mathematics - II_\n"
                    "- _Engineering Physics_\n"
                    "- _Engineering Graphics_\n"
                    "- _Engineering Chemistry_\n"
                    "- _Engineering Mechanics_\n"
                    "- _Basic Electrical Engineering_\n"
                    "- _Basic Electronics Engineering_\n"
                    "- _Programming and Problem Solving_")
        elif "second year" in user_input.lower():
            st.session_state.subjects_requested = False  # Reset after responding
            return ("_Following are your subjects for Semester 3:_\n\n"
                    "- _Computer Graphics_\n"
                    "- _Discrete Mathematics_\n"
                    "- _Object Oriented Programming_\n"
                    "- _Fundamentals of Data Structures_\n"
                    "- _Digital Electronics and Logic Design_\n\n"
                    "_Semester 4:_\n\n"
                    "- _Microprocessor_\n"
                    "- _Mathematics III_\n"
                    "- _Software Engineering_\n"
                    "- _Data Structures & Algorithms_\n"
                    "- _Principles of Programming Languages_")
        elif "third year" in user_input.lower():
            st.session_state.subjects_requested = False  # Reset after responding
            return ("_Following are your subjects for Semester 5:_\n\n"
                    "- _Theory of Computation_\n"
                    "- _Database Management Systems_\n"
                    "- _Computer Networks and Security_\n"
                    "- _Systems Programming and Operating System_\n\n"
                    "_Semester 6:_\n\n"
                    "- _Web Technology_\n"
                    "- _Artificial Intelligence_\n"
                    "- _Data Science and Big Data Analytics_")
        elif "fourth year" in user_input.lower():
            st.session_state.subjects_requested = False  # Reset after responding
            return ("_Following are your subjects for Semester 7:_\n\n"
                    "- _Data Analytics_\n"
                    "- _Mobile Communication_\n"
                    "- _High Performance Computing_\n"
                    "- _Data Mining and Warehousing_\n"
                    "- _Pervasive and Ubiquitous Computing_\n"
                    "- _Artificial Intelligence and Robotics_\n"
                    "- _Software Testing and Quality Assurance_\n\n"
                    "_Semester 8:_\n\n"
                    "- _Machine Learning_\n"
                    "- _Cloud Computing (Elective IV)_\n"
                    "- _Information and Cyber Security_\n"
                    "- _Software Defined Networks (Elective IV)_\n"
                    "- _Human Computer Interface (Elective IV)_\n"
                    "- _Soft Computing and Optimization Algorithms (Elective III)_")
        else:
            return "_Please select a valid year from the list: First Year, Second Year, Third Year, or Fourth Year._"

    # General responses
    if "about" in tokens and "college" in tokens:
        return "_ATC is devoted to establishing high standards, to educate, enrich and impart professional Engineering and Management education,_ " \
               "_by well-qualified and experienced faculty members, devoted to nurturing students into socially responsible professionals through creative collaboration, innovation, and research._"
    elif "faculty" in tokens:
        return "_Here are your teachers: Mr. SK Shinde, Mrs. Kirti Bhosale, Mrs. Jagriti Wanve, Mr. Rohit Deshmukh, and Mr. Atul Khedkar._"
    else:
        return random.choice([
            "_How can I assist you today?_",
            "_Is there anything I can do for you?_",
            "_Do you need help with something?_",
        ])

# HTML code for the center-aligned title and logo
def display_logo_and_heading(logo_img):
    st.markdown(
        f"""
        <div style='display: flex; justify-content: center; align-items: center;'>
            <img src='data:image/jpeg;base64,{logo_img}' alt='logo' style='width: 50px; height: 50px; margin-right: 10px;'>
            <h1 style='margin: 0;'>Adsul Technical Campus Bot</h1>
        </div>
        """, unsafe_allow_html=True
    )

# Convert image to base64 for embedding
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Path to your logo
logo_path = "C:\\Users\\DELL\\OneDrive\\Desktop\\Clients\\A2- Akshay\\code\\assets\\logo2.png"
logo_img = get_base64_image(logo_path)

# Check if the user is logged in
if "logged_in_user" in st.session_state:
    username = st.session_state["logged_in_user"]
    greeting = get_greeting()

    # Display the centered heading and logo
    display_logo_and_heading(logo_img)

    # Add spacing below the heading
    st.markdown("<br><br>", unsafe_allow_html=True)  # Adding vertical space

    # Initialize chat history and user avatar if not present
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.subjects_requested = False  # Add a flag for subject requests
        st.session_state.user_avatar = "avataaars"  # Set a consistent human-like avatar for the user
        # Add greeting message to chat history if it's the first login
        st.session_state.messages.append({"role": "assistant", "content": f"*Hi {username}! {greeting}! Is there anything I can do for you?*"})

    # Display chat messages from history using message() function
    for i in range(len(st.session_state.messages)):
        msg = st.session_state.messages[i]
        if msg["role"] == "assistant":
            message(msg["content"], avatar_style="lorelei", key=f"assistant_{i}")  # Bot response with Lorelei avatar
        else:
            message(msg["content"], is_user=True, avatar_style=st.session_state.user_avatar, key=f"user_{i}")  # User response aligned right with unique key

    # Accept user input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Display user message in chat message container with unique key
        message(prompt, is_user=True, avatar_style=st.session_state.user_avatar, key=f"user_{len(st.session_state.messages)}")

        # Generate chatbot response based on user input
        response = response_generator(prompt)

        # Display chatbot response in italics with unique key
        message(f"{response}", avatar_style="lorelei", key=f"assistant_{len(st.session_state.messages)}")  # Bot response with Lorelei avatar

        # Add chatbot response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})  # Store without additional asterisks
else:
    st.write("You are not logged in. Please login first.")
    st.warning("Redirecting to login page...")
    st.rerun()
