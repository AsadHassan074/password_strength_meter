import streamlit as st
import re

def check_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~" + r'"]', password) is None

    score = 5 - sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error])

    if score == 5:
        return "Strong 💪🔥", "green"
    elif score >= 3:
        return "Moderate 😐", "orange"
    else:
        return "Weak 😢", "red"


st.set_page_config(page_title="Password Strength Meter", page_icon="🔐", layout="centered")

st.title("🔐 Password Strength Meter")
st.markdown("Check how strong your password is! 🔍")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, color = check_strength(password)
    st.markdown(f"### Strength: <span style='color:{color}'>{strength}</span>", unsafe_allow_html=True)

    st.markdown("### Password Tips 🛡️")
    st.markdown("- Use **8 or more characters**")
    st.markdown("- Include **uppercase & lowercase** letters")
    st.markdown("- Add **numbers** and **symbols**")
else:
    st.info("Please enter a password to check its strength 🔎")

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")

