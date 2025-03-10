import streamlit as st
import random
import string

# Common weak passwords
COMMON_PASSWORDS = ["123456", "password", "password123", "qwerty", "abc123", "letmein", "12345678"]

#  Custom css 
st.markdown(
    """
    <style>
        /* Force Full-Page Background */
        [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #3a3a52, #4a4f6b);

            color: white;
            font-family: 'Poppins', sans-serif;
        }

        /* Centered Title */
        .title {
            text-align: center; 
            font-size: 42px; 
            font-weight: bold; 
            color: #ffae00; 
            text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.3);
        }

        /* Customizing Buttons */
        .stButton>button {
            background: linear-gradient(90deg, #ff4b4b, #ffae00);
            color: white;
            padding: 12px 20px;
            font-size: 18px;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            transition: 0.3s;
        }

        .stButton>button:hover {
            background: linear-gradient(90deg, #ffae00, #ff4b4b);
            box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.4);
        }

        /* Password Box */
        .password-box {
            background: rgba(255, 255, 255, 0.2);
            padding: 15px;
            border-radius: 12px;
            box-shadow: 2px 2px 10px rgba(255, 255, 255, 0.2);
            font-size: 18px;
            text-align: center;
        }

        /* Copy Button */
        .copy-btn {
            background: #00c2ff;
            color: white;
            padding: 8px 15px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: 0.3s;
        }

        .copy-btn:hover {
            background: #0077ff;
        }

    </style>
    """,
    unsafe_allow_html=True,
)

# 🏆 Title
st.markdown("<h1 class='title'>🔐 Next-Level Password Strength Checker 🚀</h1>", unsafe_allow_html=True)

# Password Strength Checker
def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("📏 Use at least **8 characters**.")

    # Uppercase & lowercase letters
    if any(char.islower() for char in password) and any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("🔠 Mix **uppercase & lowercase** letters.")

    # Digits
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("🔢 Add **some numbers**.")

    # Special characters
    if any(char in "!@#$%^&*()_+" for char in password):
        score += 1
    else:
        suggestions.append("😎 Use **special characters** (!@#$%^&*).")

    # Check common passwords
    if password in COMMON_PASSWORDS:
        return 0, ["🚨 **Too common!** Choose something unique."]

    return score, suggestions

# 🎲 Generate Strong Password
def generate_strong_password(length=12, use_digits=True, use_symbols=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()_+"
    return "".join(random.choice(chars) for _ in range(length))

# 📝 Password Input
password = st.text_input("🔑 **Enter your password:**", type="password")

if st.button("💥 Check Strength", key="check"):
    if password:
        score, feedback = check_password_strength(password)

        # 🌈 Animated Strength Meter
        st.progress(score / 5)

        if score == 0:
            st.error("😨 Very Weak!")  # Fix: Only main message

        elif score == 1:
            st.warning("😬 Weak! Needs improvement.")
        elif score == 2:
            st.info("😐 Moderate! Consider adding variety.")
        elif score == 3:
            st.success("🔥 Strong! Almost there.")
        else:
            st.balloons()
            st.success("💪 Ultra Strong! Your password is awesome! 🚀")

        # Suggestions (If Needed)
        if feedback:
            st.markdown("<div class='suggestion-box'><b>🔎 Improve Your Password:</b>", unsafe_allow_html=True)
            for tip in feedback:
                st.write(f"- {tip}")
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("⛔ **Please enter a password!**")

# 🎲 Advanced Password Generator
st.markdown("### 🎲 Generate a Strong Password")
length = st.slider("🔢 Password Length", 8, 20, 12)
use_digits = st.checkbox("🔢 Include Numbers", value=True)
use_symbols = st.checkbox("💎 Include Special Characters", value=True)

if st.button("🔥 Generate"):
    strong_password = generate_strong_password(length, use_digits, use_symbols)
    st.code(strong_password, language="text")

    # ✅ Copy to Clipboard Feature Fix
    st.markdown(
        f"""
        <input type="text" value="{strong_password}" id="password_copy" readonly 
        style="position: absolute; left: -9999px;">
        """,
        unsafe_allow_html=True,
    )

# 🔥 Add Pro Tip
st.markdown("---")
st.info("🔒 **Pro Tip:** Use a **password manager** to keep track of strong passwords!")