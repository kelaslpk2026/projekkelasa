import streamlit as st



st.set_page_config(
    page_title="Finance Dashboard",
    layout="wide"
)

option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

# Dummy database user
USERS = {
    "admin": "12345",
    "user": "abcde"
}

# Dummy chatbot
def finance_bot(prompt):
    return f"FinanceBot menjawab: {prompt}"

# Session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "messages" not in st.session_state:
    st.session_state.messages = []

# UI
st.title("📊 Dashboard")
st.header("Laporan Bulanan")
st.subheader("📈 Monthly Expenses")
st.caption("Made with ❤️ using Streamlit")

# Login
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if USERS.get(username) == password:
        st.session_state.authenticated = True
        st.session_state.username = username
        st.success("Login berhasil")
        st.rerun()
    else:
        st.error("Invalid credentials")

# Setelah login
if st.session_state.authenticated:

    st.write(f"Selamat datang, {st.session_state.username}")

    st.chat_message("assistant").write(
        "Hi! Saya FinanceBot."
    )

    # Tampilkan history
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(
            msg["content"]
        )

    # Input chat
    prompt = st.chat_input(
        "Tulis pertanyaan Anda..."
    )

    if prompt:

        # Simpan user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        st.chat_message("user").write(prompt)

        # Bot response
        response = finance_bot(prompt)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        st.chat_message("assistant").write(response)

import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
with col3:
    st.header("Fitur 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")
