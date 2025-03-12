import streamlit as st

# Set dark theme
st.set_page_config(page_title="DERM-AI", layout="wide")

# Custom CSS for chat-like appearance
st.markdown("""
    <style>
        .stChatMessage {
            background-color: #444;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 10px;
        }
        .stChatMessage.user {
            background-color: #1E90FF;
            color: white;
        }
        .stChatMessage.bot {
            background-color: #222;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("DERM-AI")
uploaded_file = st.sidebar.file_uploader("Upload an Image", type=["webp", "png", "jpeg", "jpg"])

# Chatbot UI
st.title("DERM-AI Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    st.markdown(f'<div class="stChatMessage {message["role"]}">{message["text"]}</div>', unsafe_allow_html=True)

# User input using chat_input
user_input = st.chat_input("Ask me anything about skin health...")
if user_input:
    st.session_state.chat_history.append({"role": "user", "text": user_input})
    response = "This is a placeholder response. Your AI model can generate an actual reply."
    st.session_state.chat_history.append({"role": "bot", "text": response})
    st.rerun()
