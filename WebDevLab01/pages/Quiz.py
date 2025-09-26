import streamlit as st
import pandas as pd

def show_title_and_intro():
    st.title("Which Type of Student Are You? ")
    st.write("Answer the questions below to find out your student style!")

def ask_question_1():
    return st.radio(   #NEW
        "How do you prefer to study for exams?",
        ["Cram the night before", "Study gradually", "Study with friends", "Don’t study"]
    )

def ask_question_2():
    return st.multiselect(   #NEW
        "Which of these study tools do you use?",
        ["Flashcards", "Lecture notes", "Online videos", "Study apps", "Practice problems"]
    )

def ask_question_3():
    return st.slider(   #NEW
        "On a scale of 1-10, how organized are your assignments?",
        1, 10, 5
    )

def ask_question_4():
    return st.number_input(   #NEW
        "How many hours per week do you spend studying outside of class?",
        min_value=0, max_value=60
    )

def ask_question_5():
    st.write("Pick the study environment you like best:")

    choice = st.radio(   #NEW
        "Which study environment do you prefer?",
        ["Quiet library", "Coffee shop", "Dorm room", "Outdoors"]
    )

    if choice == "Quiet library":
        st.image("Images/library.jpg")   #NEW
    elif choice == "Coffee shop":
        st.image("Images/coffee.jpg")   #NEW
    elif choice == "Dorm room":
        st.image("Images/dorm.jpg")   #NEW
    elif choice == "Outdoors":
        st.image("Images/outdoor.jpg")   #NEW

    return choice 

def show_result(q1, q2, q3, q4, q5):
    if st.button("Get My Student Style"):   #NEW
        st.write("Here’s your student style based on your answers!")
        if q1 == "Cram the night before" and q3 < 5:
            st.success("Last-Minute Crammer")   #NEW
        elif "Flashcards" in q2 or q4 > 15:
            st.success("The Dedicated Learner")   #NEW
        elif q5 == "Coffee shop":
            st.success("The Social Studier")
        else:
            st.success("The Balanced Student")

show_title_and_intro()
q1 = ask_question_1()
st.write("---")
q2 = ask_question_2()
st.write("---")
q3 = ask_question_3()
st.write("---")
q4 = ask_question_4()
st.write("---")
q5 = ask_question_5()
st.write("---")
show_result(q1, q2, q3, q4, q5)
