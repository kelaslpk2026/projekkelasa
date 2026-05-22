import streamlit as st

st.title(":blue[Kalkulator Aritmatika Kelas A]:rocket:")
st.header("*Kalkulator*  **Aritmatika** ***Sederhana***.")
number = st.number_input("Masukkan Angka",min_value=0)
satu,dua,tiga,empat,lima=st.columns(5)
if satu.button("Faktorial"):
    number = int(number)
    st.subheader(math.factorial(number))
elif dua.button("Akar Kuadrat"):
    st.subheader(math.sqrt(number))
elif tiga.button("Kuadrat") :
    st.subheader(number**2)
elif empat.button("Logaritma") :
    st.subheader(math.log(number))
elif lima.button("Ln"):
    st.subheader(math.ln(number))
if st.button("reset"):
    st.rerun()
