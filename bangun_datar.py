import math

# 1. Persegi
def luas_persegi(sisi):
    return sisi * sisi

# 2. Segitiga
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

# 3. Lingkaran
def luas_lingkaran(jari_jari):
    return math.pi * jari_jari * jari_jari

# 4. Belah ketupat
def luas_ketupat(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

# 5. Jajar genjang
def luas_jajar_genjang(panjang, lebar):
    return panjang * lebar