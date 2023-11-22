import datetime
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd
from PIL import Image

st.write(
    """
    # Hi! Welcome to Rifqi's Room
    Here you can see many things about Rifqi
    """
)

st.title('Moments')
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Music")
    image = Image.open('IMG_20231116_015807.jpg')
    st.image(image, caption='Coldplay Jakarta: Music of the Spheres')
with col2:
    st.header("Aviation")
    image = Image.open('IMG_20230821_130931.jpg')
    st.image(image, caption='Cockpit Visit: Jetstar Asia')
with col3:
    st.header("Football")
    image = Image.open('VID_20230930_182700.00_00_06_07.Still001_removedsponsored.png')
    st.image(image, caption='National Youth Training Centre Sawangan')

st.title("Get to Know Rifqi")
st.header("Personal Stats")
st.subheader("Try it with Python!")
st.text("Hi, wanna try to greet Rifqi? Copy this code below into your Python!")
code = "print('Hello, Rifqi!')"
st.code(code, language='python')

st.subheader("Data Science Path")
st.text("He is now learning Data Science with Dicoding Platform. See what he has done so far!")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
st.line_chart(
   chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
)
st.text("Yap! That was just a random line chart :D")
st.text("Don't worry! Rifqi will have got it with a real new one soon.")

st.subheader("Average of Rifqi's grade in class")
st.text("You can find it out soon after he updates the data.")
st.text("But don't worry, you are still able to take a note of this following equation of average:")
st.latex(r"""
    Average={\frac {1}{n}}\sum _{i=1}^{n}a_{i}={\frac {a_{1}+a_{2}+\cdots +a_{n}}{n}}
""")
st.write("For a sneak peek, he has improved his grade in his 4th term.")
st.metric(label="GP", value="3.36", delta="0.14")
st.write("Let's hope for him to get the best in this term.")

st.title("Get to Know Yourself")
st.header("He wants to know about you   ")
st.subheader("Fill with yours!")
name = st.text_input(label='Nickname', value='')
st.write('Name: ', name)
text = st.text_area('Is there anything you\'d like to say to him?', value='')
st.write('To Rifqi: ', text)
number = st.number_input(label='How old are you?')
st.write('Age: ', int(number), ' years old')
date = st.date_input(label='Date of Birth', min_value=datetime.date(1900, 1, 1))
st.write('Date of Birth:', date)

if st.button('Greeting Button'):
    st.write('Hi, there! Thanks for pushing it.')
agree = st.checkbox('I agree')
if agree:
    st.write('Welcome to Rifqi\'s App')

st.subheader("Make it with choices!")

genre = st.radio(
    label="What's your gender",
    options=('Male', 'Female', 'Prefer not to say'),
    horizontal=True
)

genre = st.selectbox(
    label="What do you do?",
    options=('Student', 'Work', 'Freelance')
)

genre = st.multiselect(
    label="What's your interest? (You can select multiple)",
    options=('Sports', 'Computing', 'Science', 'Engineering', 'Health', 'Art')
)

st.title("Documentation")
st.header("Growing Up Rifqi")
st.title('Belajar Analisis Data')
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
with tab1:
    st.header("Junior High School")
    image = Image.open('IMG_20180627_202127.jpg')
    st.image(image, caption='Bento JHS Graduation')
with tab2:
    st.header("Senior High School")
    image = Image.open('IMG_2026.JPG')
    st.image(image, caption='Smanti at its Batik')
with tab3:
    st.header("College")
    image = Image.open('DSC_0559 edited.png')
    st.image(image, caption='Universitas Indonesia')

with st.container():
    st.header("Moment of the Year")
    image = Image.open('IMG_20231116_015807.jpg')
    st.image(image, caption='Coldplay Jakarta: Music of the Spheres')
with st.expander("See explanation"):
    st.write(
        """I\'ve been listening Coldplay since I was in the elementary school. 
        In that time, Viva La Vida, Fix You, and Paradise were the most listening music of Coldplay songs. 
        When I heard that Coldplay were about to coming to Indonesia, I was like \'WOW\'. 
        Dream comes true, I watched tshem directly with my eyes and guess what... 
        Now I have a PCD (Post Concert Depression) where I couldn\'t move on yet from it.
        Thanks for reading.
        """
    )