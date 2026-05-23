import streamlit as st

st.set_page_config(
    page_title="Finance Dashboard",
    layout="wide"
)

# Dummy database user
USERS = {
    "admin": "12345",
    "user": "abcde"
}

# UI
st.title("📊 Dashboard")
st.header("Laporan Bulanan")
st.subheader("📈 Monthly Expenses")
st.caption("Made with ❤️ using Streamlit")

# Session state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Input login
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Login button
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
