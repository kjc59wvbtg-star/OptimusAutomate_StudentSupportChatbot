import streamlit as st
import json
import random

with open("intents.json", "r") as file:
    data = json.load(file)

st.set_page_config(
    page_title="AI Student Support Chatbot",
    page_icon="🤖"
)

st.title("🤖 AI Student Support Chatbot")
st.write("Ask me about courses, fees, duration, or greetings.")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "context" not in st.session_state:
    st.session_state.context = None

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = "Sorry, I don't understand."

    user_input_lower = user_input.lower()

    for intent in data["intents"]:

        for pattern in intent["patterns"]:

            if pattern.lower() in user_input_lower:

                response = random.choice(
                    intent["responses"]
                )

                st.session_state.context = intent["tag"]
                break

    if (
        "duration" in user_input_lower
        and st.session_state.context == "courses"
    ):
        response = "Most courses range from 3 to 6 months."

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    st.rerun()