
'''
import streamlit as st
from art import text2art

# Streamlit app
st.title("Text to ASCII Art Generator")
st.write("Enter text to generate ASCII art")

# Get user input
user_input = st.text_input("Enter text")

# Generate ASCII art
if user_input:
    ascii_art = text2art(user_input)
    st.write("Generated ASCII Art:")
    st.code(ascii_art)
    '''
import streamlit as st
from art import text2art
import random

# Streamlit app
st.title("Text to ASCII Art Generator")
st.write("Enter text to generate ASCII art")

# Get user input
user_input = st.text_input("Enter text")

# Generate ASCII art
if user_input:
    ascii_art = text2art(user_input)
    st.write("Generated ASCII Art:")
    st.code(ascii_art)

# Random button
if st.button("Random"):
    styles = ["standard", "script", "slant", "romanc", "bubble", "digital", "block", "banner", "isometric1", "isometric2"]
    for _ in range(10):
        random_style = random.choice(styles)
        try:
            random_art = text2art(user_input, font=random_style)
            st.write(f"Style: {random_style}")
            st.code(random_art)
        except Exception as e:
            st.write(f"Error generating art for style {random_style}: {e}")
    
    # Save ASCII art to a file
    if user_input:
        with open('ascii_art.txt', 'w') as file:
            file.write(ascii_art)
