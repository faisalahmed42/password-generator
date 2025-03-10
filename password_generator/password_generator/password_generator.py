import streamlit as st
import random
import string

# Password Generator Function
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  # letters (A-Z, a-z)

    if use_digits:
        characters += string.digits  # numbers (0-9)

    if use_special:
        characters += string.punctuation  # Special characters

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit Application UI
st.title("🔑 Password Generator")

# Password Length Slider
length = st.slider("Select Password Length", min_value=6, max_value=32, value=12)

# Checkboxes for digits and special characters
use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

# Password Generator Button
if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"Generated Password: `{password}`")

st.write("Built with ❤️ by [Faisal Ahmed](https://github.com/faisalahmed007)")
