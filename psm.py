import re
import streamlit as st

# Page Styling
st.set_page_config(
    page_title='Password Strength Meter', 
    page_icon='🔒', 
    layout='centered', 
    initial_sidebar_state='expanded'
)

# Custom CSS for better UI
st.markdown(
    """
    <style>
        .main {text-align: center;}
        .stTextInput {width: 60% !important; margin: 0 auto;}
        .stButton {width: 60% !important; margin: 0 auto; background-color: #4CAF50; color: white; font-weight: bold;}
        .stButton:hover {background-color: #45a049;}
        .stAlert {text-align: center; font-weight: bold;}
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title and Description
st.title('🔒 Password Strength Meter')
st.write('''This tool checks your password strength based on:
- ✅ At least **8 characters** long
- ✅ Contains **uppercase & lowercase letters**
- ✅ Includes **at least one number** (0-9)
- ✅ Has **at least one special character** (!@#$%^&* etc.)
''')

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔹 Password should be **at least 8 characters long**.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔹 Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔹 Password should include **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*()_+={};:'\"<>,.?/~`|-]", password):
        score += 1
    else:
        feedback.append("🔹 Password should include **at least one special character** (!@#$%^&* etc.).")
    
    # Display Password Strength Result
    if score == 4:
        st.success("✅ **Strong Password!** Your password is secure.")
    elif score == 3:
        st.info("🟡 **Moderate Password!** Consider improving it by adding more elements.")
    else:
        st.error("❌ **Weak Password!** Follow the suggestions below to strengthen it.")

    # Display Feedback
    if feedback:
        with st.expander("💡 Suggestions to Improve Your Password"):
            for item in feedback:
                st.markdown(f"- {item}")

# Input Field for Password
password = st.text_input("🔑 Enter Your Password", type="password", help="Enter your password to check its strength.")

# Button to Check Password Strength
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password to check its strength.")
