import streamlit as st
st.title("From Data Diri")
st.write("isi data pribadi")
st.write("Made By Devandra")

with st.form("form_data_diri"):
    nama = st.text_input("nama")
    alamat = st.text_input("alamat")
    usia = st.text_input("usia")
    submit = st.form_submit_button("submit")

    
if submit:
    st.write(f"Halo Nama Gua {nama} Gua Tinggal Di {alamat} Umur Gua {usia}")