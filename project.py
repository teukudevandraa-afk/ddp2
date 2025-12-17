# Program Konversi Mata Uang
# Rupiah <-> Dollar

# Misalkan 1 USD = 15.500 Rupiah (bisa diganti sesuai kurs terbaru)
import streamlit as st

st.header("penkonversian mata uang")

KURS_USD = 15500

def rupiah_ke_dollar(rupiah):
    return rupiah / KURS_USD

def dollar_ke_rupiah(dollar):
    return dollar * KURS_USD

def main():
    print("=== Program Konversi Mata Uang Rupiah <-> Dollar ===")
    print("1. Konversi Rupiah ke Dollar")
    print("2. Konversi Dollar ke Rupiah")
    
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == "1":
        rupiah = float(input("Masukkan jumlah Rupiah: "))
        hasil = rupiah_ke_dollar(rupiah)
        print(f"{rupiah:,.0f} Rupiah = ${hasil:,.2f} Dollar")

    elif pilihan == "2":
        dollar = float(input("Masukkan jumlah Dollar: "))
        hasil = dollar_ke_rupiah(dollar)
        print(f"${dollar:,.2f} Dollar = {hasil:,.0f} Rupiah")

    else:
        print("Pilihan tidak valid!")




# Jalankan program
main()

# def inputan():
#     st.header("Konversi mata uang")

#     with st.form('myform'):
#         KURS_USD = 15500
#         mata_uang = st.text_input("Mata Uang")
#         if mata_uang == "dolar":
#             jumlah = st.number_input("", value=None)
#             hasil = jumlah * KURS_USD