import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Khaleah's 2026 Dashboard", page_icon="🧶")

# Title
st.title("Khaleah's 2026 Growth Hub 🚀")

# 2026 Progress Bar
st.subheader("Yearly Progress")
day_of_year = datetime.now().timetuple().tm_yday
percent_passed = round((day_of_year / 365) * 100, 1)
st.write(f"We are **{percent_passed}%** through 2026!")
st.progress(percent_passed / 100)

# --- NEW SECTION: Crochet Gallery ---
st.divider()
st.subheader("🧶 Khaleah's Crochet Portfolio")

# This lets you pick a photo from your computer
uploaded_file = st.file_uploader("Upload a photo of your latest work!", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # This displays the image you just uploaded
    st.image(uploaded_file, caption="Latest Creation", use_container_width=True)
    st.success("That looks amazing! Your tension is perfect. ✨")
else:
    st.info("Upload a file to see your work here!")
# Python Task List
st.divider()
st.subheader("🐍 Python Learning Path")
st.checkbox("Fixed my Environment Path", value=True)
st.checkbox("Ran 'streamlit hello'", value=True)
st.checkbox("Launched my first custom app")

if st.button("Celebrate!"):
    st.balloons()
# --- NEW SECTION: Budget Tracker ---
st.divider()
st.subheader("💰 2026 Financial Goal: No-Spend Tracker")

# Create a small interactive calculator
monthly_income = st.number_input("Enter Monthly Income ($):", value=1000)
needs = monthly_income * 0.5
wants = monthly_income * 0.3
savings = monthly_income * 0.2

st.write(f"Based on your **50/30/20** goal:")
st.info(f"📍 Needs: ${needs} | 📍 Wants: ${wants} | 💰 Savings: ${savings}")

# No-Spend Progress
days_spent = st.slider("How many days have you successfully avoided extra spending?", 0, 31, 10)
if days_spent >= 20:
    st.success(f"Amazing! You've hit {days_spent} days. You're crushing the wealth gap! 📈")
else:
    st.warning(f"You're at {days_spent} days. Keep pushing for that 10% increase!")

import random # This must be at the very top of your file!

# --- NEW SECTION: The Randomizer ---
st.divider()
st.subheader("🎲 The Decision Maker")
st.write("Can't decide what to do next? Let Python choose!")

# Create a list of your current 2026 interests
options = [
    "🐍 Learn a new Python function",
    "🧶 Crochet 5 more rows of my project",
    "📚 Read a chapter of 'Animal Farm'",
    "🎧 Practice Active Listening for 10 minutes",
    "💰 Update my 50/30/20 budget"
]

if st.button("Choose My Next Task"):
    # This is the "Magic" line that picks one item from the list
    choice = random.choice(options)
    
    st.balloons()
    st.info(f"The Universe (and Python) says you should: **{choice}**")
   # --- NEW SECTION: The Secret Vault ---
st.divider()
st.subheader("🔐 Khaleah's Secret Vault")

# Create a password input (it hides the text you type)
password = st.text_input("Enter your Secret Key to unlock:", type="password")

# Pick a secret key (I used 'crochet2026', but you can change it!)
if password == "crochet2026":
    st.success("Access Granted! Welcome back, Khaleah.")
    
    # Everything inside this 'if' block is HIDDEN until the password is right
    st.markdown("### 📝 Private Journal & Reflection")
    
    # A place to log your "Active Listening" or "Negotiation" wins
    entry = st.text_area("What did you learn today?")
    if st.button("Save Entry"):
        st.write("Entry saved to your session! (Next step: learning databases!)")
        
    st.info("💡 Tip: Only you can see this section because only you know the key.")

elif password != "":
    st.error("Access Denied. Incorrect key.") 
# --- CORRECTED SECTION: 2026 Reading Challenge ---
st.divider()
st.subheader("📚 2026 Reading List")

col_book1, col_book2 = st.columns(2)

with col_book1:
    st.markdown("#### *Bring Me Your Midnight*")
    # This book has 32 chapters
    bmym_chapters = st.slider("Chapters read (Midnight):", 0, 32, 5)
    bmym_progress = (bmym_chapters / 32)
    st.progress(bmym_progress)
    st.write(f"🌙 {int(bmym_progress * 100)}% Complete")

with col_book2:
    st.markdown("#### *Swimming in a Sea of Stars*")
    # This book has 35 chapters
    stars_chapters = st.slider("Chapters read (Sea of Stars):", 0, 35, 10)
    stars_progress = (stars_chapters / 35)
    st.progress(stars_progress)
    st.write(f"⭐ {int(stars_progress * 100)}% Complete")

# Celebration for finishing!
if bmym_chapters == 32 or stars_chapters == 35:
    st.balloons()
    st.success("You finished a 2026 favorite! Your reading goal is on fire. 🔥")
