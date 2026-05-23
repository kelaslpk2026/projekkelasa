import streamlit as st
# app.py — baris 13
st.set_page_config(
  page_title="Finance Dashboard",
  layout="wide"
)

# Hirarki teks
st.title("📊 Dashboard")
st.header("Laporan Bulanan")
st.subheader("📈 Monthly Expenses")
st.caption("Made with ❤️ using Streamlit")
# Inisialisasi session_state
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Login check
if st.button("Login"):
    if USERS.get(username) == password:
        st.session_state.authenticated = True
        st.session_state.username = username
        st.rerun()
    else:
        st.error("Invalid credentials")
