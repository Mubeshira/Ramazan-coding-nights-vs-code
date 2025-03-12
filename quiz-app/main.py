# import streamlit as st # for the web interface
# import random # for randomizing the questions
# import time # for the timer

# # Title of the Application
# st.title("📝 Quiz Application")

# # Define quiz questions, options, and answer in the form of a list of dictionaries
# questions = [
#         {
#         "question": "What is the capital of France?",
#         "options": ["Paris", "London", "Berlin", "Lisbon"],
#         "answer": "Paris"
#     },
#     {
#         "question": "What is the capital of Germany?",
#         "options": ["Paris", "London", "Berlin", "Lisbon"],
#         "answer": "Berlin"
#     },
#     {
#         "question": "What is the capital of Portugal?",
#         "options": ["Paris", "London", "Berlin", "Lisbon"],
#         "answer": "Lisbon"
#     },
#     {
#         "question": "What is the capital of Spain?",
#         "options": ["Paris", "London", "Berlin", "Lisbon"],
#         "answer": "Lisbon"
#     },
#     {
#         "question": "What is the capital of Italy?",
#         "options": ["Paris", "London", "Rome", "Lisbon"],
#         "answer": "Rome"
#     },
#     {
#         "question": "What is the capital of the United Kingdom?",
#         "options": ["Paris", "London", "Berlin", "Lisbon"],
#         "answer": "London"
#     },
#     {
#         "question": "What is the capital of the United States?",
#         "options": ["Paris", "Washington DC", "Berlin", "Lisbon"],
#         "answer": "Washington DC"
#     },
#     {
#         "question": "What is the capital of Canada?",
#         "options": ["Paris", "London", "Berlin", "Ottawa"],
#         "answer": "Ottawa"
#     },
    
#     {
#         "question": "What is the capital of Japan?",
#         "options": ["Paris", "London", "Tokyo", "Lisbon"],
#         "answer": "Tokyo"
#     }
# ]

# # Initialize a random question if none exists in the session state
# if "current_question" not in st.session_state:
#     st.session_state.current_question = random.choice(questions)

# # Get the current question from session state
# question = st.session_state.current_question

# # Display the question
# st.subheader(question["question"])

# # Create radio buttons for the options
# selected_option = st.radio("Choose your answer", question["options"], key="answer")

# # Submit button the check the answer
# if st.button("Submit Answer"):
#     # check if the answer is correct
#     if selected_option == question["answer"]:
#         st.success("✅ Correct! 🎉")
#         st.balloons()
#     else:
#         st.error("❌ Incorrect! ☹️ the correct answer is " + question["answer"])
  
#     # Wait for 3 seconds before showing the next question
#     time.sleep(2)

#     # Select a new random question
#     st.session_state.current_question = random.choice(questions)

#     # Rerun the app to display the next question    
#     st.rerun()


import streamlit as st  # for the web interface
import random  # for randomizing the questions
import time  # for the timer

# Custom CSS for black background and styled fonts
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
        font-family: Arial, sans-serif;
    }
    .stApp {
        background-color: white;
    }
    .stTextInput, .stButton, .stRadio {
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the Application
st.title("📝 Quiz Application")


# Define quiz questions, options, and answer in the form of a list of dictionaries
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Lisbon"], "answer": "Paris"},
    {"question": "What is the capital of Germany?", "options": ["Paris", "London", "Berlin", "Lisbon"], "answer": "Berlin"},
    {"question": "What is the capital of Portugal?", "options": ["Paris", "London", "Berlin", "Lisbon"], "answer": "Lisbon"},
    {"question": "What is the capital of Spain?", "options": ["Paris", "London", "Berlin", "Lisbon"], "answer": "Lisbon"},
    {"question": "What is the capital of Italy?", "options": ["Paris", "London", "Rome", "Lisbon"], "answer": "Rome"},
    {"question": "What is the capital of the United Kingdom?", "options": ["Paris", "London", "Berlin", "Lisbon"], "answer": "London"},
    {"question": "What is the capital of the United States?", "options": ["Paris", "Washington DC", "Berlin", "Lisbon"], "answer": "Washington DC"},
    {"question": "What is the capital of Canada?", "options": ["Paris", "London", "Berlin", "Ottawa"], "answer": "Ottawa"},
    {"question": "What is the capital of Japan?", "options": ["Paris", "London", "Tokyo", "Lisbon"], "answer": "Tokyo"}
]

# Initialize a random question if none exists in the session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Get the current question from session state
question = st.session_state.current_question

# Display the question
st.subheader(question["question"])

# Create radio buttons for the options
selected_option = st.radio("Choose your answer", question["options"], key="answer")

# Submit button to check the answer
if st.button("Submit Answer"):
    # Check if the answer is correct
    if selected_option == question["answer"]:
        st.success("✅ Correct! 🎉")
        st.balloons()
    else:
        st.error(f"❌ Incorrect! ☹️ The correct answer is {question['answer']}")
    
    # Wait for 3 seconds before showing the next question
    time.sleep(2)

    # Select a new random question
    st.session_state.current_question = random.choice(questions)

    # Rerun the app to display the next question
    st.rerun()



st.markdown("### 🎉 Made by Mubeshira Saad")