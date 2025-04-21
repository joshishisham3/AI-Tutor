import streamlit as st
import random  # best to keep imports at the top

st.title("Hello, Everyone!")
st.write("This is your first Streamlit app.")
st.write("Hello everyone this is Shisham Joshi. I am writing this code to build a simple application software. Thank you :)")

st.title("AI Mini-Tutor for Junior Kids")
st.write("Learn English, Nepali, and Fun Facts with AI!")

# Get user name
name = st.text_input("What's your name?")

if name:
    st.write(f"Hi {name}! Let's start learning 🎉")

    # Quiz section
    st.subheader("Mini Quiz: English Vocabulary")
    question = st.radio("What is the Nepali word for 'Sun'?", ["Jun", "Surya", "Tara", "Pani"])

    if question:  # Once an option is selected
        if question == "Surya":
            st.success("Correct! ☀️ Surya means Sun in Nepali.")

            # Now show Word of the Day and Fun Fact
            words = [
                {"english": "River", "nepali": "Nadi"},
                {"english": "Tree", "nepali": "Rukh"},
                {"english": "Water", "nepali": "Pani"},
            ]
            word = random.choice(words)
            st.subheader("📖 Word of the Day")
            st.write(f"**English:** {word['english']}  —  **Nepali:** {word['nepali']}")

            fun_facts = [
                "Did you know? Elephants can’t jump!",
                "A group of frogs is called an army 🐸",
                "Mount Everest is called Sagarmatha in Nepali 🏔️"
            ]
            st.subheader("🌟 Fun Fact")
            st.info(random.choice(fun_facts))

            # Positive message
            st.write(f"Good job, {name}! You’re doing great. Keep learning every day! 🌱")

        else:
            st.error("Oops! Try again.")
