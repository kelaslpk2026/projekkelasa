import streamlit as st

st.title(":blue[Kalkulator Aritmatika Kelas A]:rocket:")
st.markdown(st.header("*Kalkulator*  **Aritmatika** ***Sederhana***."))
number = st.number_input("Masukkan Angka",min_value=0)
satu,dua,tiga,empat,lima=st.columns(5)
if satu.button("Faktorial"):
    number = int(number)
    st.write(math.factorial(number))
elif dua.button("Akar Kuadrat"):
    st.write(math.sqrt(number))
elif tiga.button("Kuadrat") :
    st.write(number**2)
elif empat.button("Logaritma") :
    st.write(math.log(number))
elif lima.button("Ln"):
    st.write(math.ln(number))
if st.button("reset"):
    st.rerun()
