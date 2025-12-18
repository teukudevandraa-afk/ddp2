import streamlit as st

st.set_page_config(
    page_title="Konersi Mata Uang",
    page_icon="🌍",
    layout="centered"
)

# function
def hitung_bagi(nilai_input, kurs):
    return nilai_input / kurs

def hitung_kali(nilai_input, kurs):
    return nilai_input * kurs

# navigasi
st.sidebar.title("Navigasi")
halaman = st.sidebar.selectbox(
    "Pilih Mata Uang:",
    ( "Latar belakang","💵 IDR & USD (Amerika)", "🕌 IDR & MYR (Malaysia)", "🗾 IDR & JPY (Jepang)", "IDR & KR (Korea Selatan)")
)

st.sidebar.markdown("---")
st.sidebar.info("Tips: Anda bisa mengubah nilai 'Kurs saat ini' di menu utama agar hasil lebih akurat.")

if halaman == "Latar belakang":
    st.header("Konversi mata uang, Rupiah, Dollar , Ringgit, Yen, Won")
    st.image("mata_uang.png", width=500)
    st.write("Aplikasi konversi mata uang ini dibuat untuk memudahkan pengguna menghitung nilai tukar antarnegara dengan cepat dan akurat. Karena setiap mata uang memiliki nilai berbeda dan kurs dapat berubah setiap hari, aplikasi ini membantu pengguna—seperti wisatawan, pelaku bisnis, dan pembeli online—untuk mengetahui harga sebenarnya tanpa perlu menghitung manual. Dengan begitu, transaksi internasional menjadi lebih mudah, praktis, dan bebas dari kesalahan perhitungan.")


# Rupiah ke dollar (DEVANDRA)
if halaman == "💵 IDR & USD (Amerika)":
    st.title("Konversi Rupiah & Dollar")
    
    # kurs usd
    col_kurs, col_space= st.columns([2,1])
    with col_kurs:
        kurs_usd = st.number_input(
            "Kurs 1 USD saat ini (dalam Rp):", 
            value=15900.0, 
            step=50.0,
            format="%.0f"
        )

    st.write("---")

 # pilih pengkorversian
    arah = st.radio(
        "Pilih Arah Konversi:",
        ["🇮🇩 Rupiah ke Dollar (IDR ➡ USD)", "🇺🇸 Dollar ke Rupiah (USD ➡ IDR)"],
        horizontal=True
    )

    # Input 
    if arah == "🇮🇩 Rupiah ke Dollar (IDR ➡ USD)":
        input_idr = st.number_input("Masukkan jumlah Rupiah (Rp):", min_value=0.0, step=10000.0)
        
        if st.button("Hitung ke USD", type="primary"):
            hasil = input_idr / kurs_usd
            st.metric(label="Hasil dalam Dollar", value=f"$ {hasil:,.2f}")
            st.caption(f"Rumus: {input_idr:,.0f} / {kurs_usd:,.0f}")

    else:
        # USD ke IDR
        input_usd = st.number_input("Masukkan jumlah Dollar ($):", min_value=0.0, step=1.0)
        
        if st.button("Hitung ke Rupiah", type="primary"):
            hasil = input_usd * kurs_usd
            st.metric(label="Hasil dalam Rupiah", value=f"Rp {hasil:,.0f}")
            st.caption(f"Rumus: {input_usd:,.2f} x {kurs_usd:,.0f}")

# rupiah ke ringgit (KEY)
elif halaman == "🕌 IDR & MYR (Malaysia)":
    st.title("Konversi Rupiah & Ringgit")

    # kurs ringgit defaulnya 3550
    col_kurs, col_space = st.columns([2,1])
    with col_kurs:
        kurs_myr = st.number_input(
            "Kurs 1 MYR saat ini (dalam Rp):", 
            value=3550.0, 
            step=10.0,
            format="%.0f"
        )

    st.write("---")

    # pilih pengkorversian
    arah = st.radio(
        "Pilih Arah Konversi:",
        ["🇮🇩 Rupiah ke Ringgit (IDR ➡ MYR)", "🇲🇾 Ringgit ke Rupiah (MYR ➡ IDR)"],
        horizontal=True
    )

    # INPUT
    if arah == "🇮🇩 Rupiah ke Ringgit (IDR ➡ MYR)":
        input_idr = st.number_input("Masukkan jumlah Rupiah (Rp):", min_value=0.0, step=10000.0)
        
        if st.button("Hitung ke MYR", type="primary"):
            hasil = input_idr / kurs_myr
            st.metric(label="Hasil dalam Ringgit", value=f"RM {hasil:,.2f}")
            st.caption(f"Rumus: {input_idr:,.0f} / {kurs_myr:,.0f}")

    # MYR ke IDR
    else: 
        input_myr = st.number_input("Masukkan jumlah Ringgit (RM):", min_value=0.0, step=10.0)
        
        if st.button("Hitung ke Rupiah", type="primary"):
            hasil = input_myr * kurs_myr
            st.metric(label="Hasil dalam Rupiah", value=f"Rp {hasil:,.0f}")
            st.caption(f"Rumus: {input_myr:,.2f} x {kurs_myr:,.0f}")

# Rupiah Ke Yen (DAPA)
elif halaman == "🗾 IDR & JPY (Jepang)":
    st.title("Konversi Rupiah & Yen")

    
    col_kurs, col_space = st.columns([2,1])
    with col_kurs:
        kurs_jpy = st.number_input(
            "Kurs 1 JPY saat ini (dalam Rp):", 
            value=107.40, 
            step=10.0,
            format="%.0f"
        )

    st.write("---")

    # Pilih pengkorversian
    arah = st.radio(
        "Pilih Arah Konversi:",
        ["🇮🇩 Rupiah ke Yen (IDR ➡ JPY)", "Yen ke Rupiah (JPY ➡ IDR)"],
        horizontal=True
    )

    # Input
    if arah == "🇮🇩 Rupiah ke Yen (IDR ➡ JPY)":
        input_idr = st.number_input("Masukkan jumlah Rupiah (Rp):", min_value=0.0, step=10000.0)
        
        if st.button("Hitung ke JPY", type="primary"):
            hasil = input_idr / kurs_jpy
            st.metric(label="Hasil dalam Yen", value=f"Yen {hasil:,.2f}")
            st.caption(f"Rumus: {input_idr:,.0f} / {kurs_jpy:,.0f}")

    # YEN ke IDR
    else:
        input_jpy = st.number_input("Masukkan jumlah Yen (JPY):", min_value=0.0, step=10.0)
        
        if st.button("Hitung ke Rupiah", type="primary"):
            hasil = input_jpy * kurs_jpy
            st.metric(label="Hasil dalam Rupiah", value=f"Rp {hasil:,.0f}")
            st.caption(f"Rumus: {input_jpy:,.2f} x {kurs_jpy:,.0f}")

# Rupiah Ke Won (AZIZAH)
elif halaman == "IDR & KR (Korea Selatan)":
    st.title("Konversi Rupiah & Won")

    
    col_kurs, col_space = st.columns([2,1])
    with col_kurs:
        kurs_kr = st.number_input(
            "Kurs 1000 KR saat ini (dalam Rp):", 
            value=11278.0, 
            step=10.0,
            format="%.0f"
        )

    st.write("---")

    # Pilih Pengkorversian
    arah = st.radio(
        "Pilih Arah Konversi:",
        ["🇮🇩 Rupiah ke Won (IDR ➡ WON)", "Won ke Rupiah (WON ➡ IDR)"],
        horizontal=True
    )

    # Input
    if arah == "🇮🇩 Rupiah ke Won (IDR ➡ WON)":
        input_idr = st.number_input("Masukkan jumlah Rupiah (Rp):", min_value=0.0, step=10000.0)
        
        if st.button("Hitung ke WON", type="primary"):
            hasil = input_idr / kurs_kr
            st.metric(label="Hasil dalam Won", value=f"Won {hasil:,.2f}")
            st.caption(f"Rumus: {input_idr:,.0f} / {kurs_kr:,.0f}")

    # Won Ke Rupiah
    else:
        input_kr = st.number_input("Masukkan jumlah Won (WON):", min_value=0.0, step=10.0)
        
        if st.button("Hitung ke Rupiah", type="primary"):
            hasil = input_kr * kurs_kr
            st.metric(label="Hasil dalam Rupiah", value=f"Rp {hasil:,.0f}")
            st.caption(f"Rumus: {input_kr:,.2f} x {kurs_kr:,.0f}")
