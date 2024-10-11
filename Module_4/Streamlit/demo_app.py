import streamlit as st
import time
import random

st.title('This is my first streamlit app!')

st.text('streamlit is lit')


with st.container(height=350):

    col1, col2, col3 = st.columns(3)

    with col1:
        name = st.text_input(
            label="Enter your name: ",
            value="",

        )

        st.write("Your name is: ", name)
    with col2:
        os_option = st.selectbox(
            "Which OS do you use to learn DL?",
            ("Windows", "MAC", "Ubuntu"),
            index=None,
            placeholder="Select an OS..."
        )

        st.write("OK, so you 're using ", os_option)
    with col3:
        dl_books = st.radio(
            "Which of following DL books you will recommend for newbie are: ",
            ("Deep learning", "Machine Learning yearning",
             "So you think you can dance"),
            captions=(
                "Author: Yann Lecun",
                "Author: Andrew Ng",
                "Author: No name"
            )
        )
        st.write("Good choice!")


def load_model():
    with st.spinner("Model is loading...."):
        time.sleep(3)
    return random.choice([True, False])


model = load_model()
if model:
    st.success("Model loaded successful")
else:
    st.error("Model loaded fail")
