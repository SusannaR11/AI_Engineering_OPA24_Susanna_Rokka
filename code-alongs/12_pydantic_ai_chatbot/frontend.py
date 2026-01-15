import streamlit as st
from chat import JokeBot

def init_session_states():
    # initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

        if "bot" not in st.session_state:
            st.session_state.bot = JokeBot()


def display_chat_messages():
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input():

    if prompt := st.chat_input("Talk to the Jokebot"):
        st.session_state.messages.append({"role": "user", "content": prompt }) #user question is saved here in session state

        bot_response = st.session_state.bot.chat(prompt).get("bot") #answer from bot

        response = f"Ro Båt: {bot_response}"

        with st.chat_message("user"): # display chat and answer
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.markdown(response)


        st.session_state.messages.append({"role": "assistant", "content": response}) # answer is saved in session state

def layout():
    st.markdown("# Chat with Ro Båt") # layout of the streamlit app
    st.write(
        "RO BÅT is a funny robot that can help you out with programming tasks. However he doesn't directly answer your question, usually he asks another question back."
    )

    display_chat_messages()
    handle_user_input()

if __name__ == "__main__":
    init_session_states()
    layout()


