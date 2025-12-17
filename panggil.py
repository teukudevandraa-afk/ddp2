import bangun_datar, bangun_ruang

print("=====Luas Bangun Datar=====")
print(f"Luas Persegi = {bangun_datar.luas_persegi(5)}")
print(f"Luas Segitiga = {bangun_datar.luas_segitiga(5, 10)}")
print(f"Luas Lingkaran = {bangun_datar.luas_lingkaran(5)}")
print(f"Luas Belah Ketupat = {bangun_datar.luas_ketupat(5, 10)}")
print(f"Luas Jajar Genjang = {bangun_datar.luas_jajar_genjang(5, 10)}")

print("=====Luas Bangun Ruang=====")
print(f"Luas Kubus = {bangun_ruang.luas_kubus(5)}")
print(f"Luas Balok = {bangun_ruang.luas_balok(5, 10, 15)}")
print(f"Luas Bola = {bangun_ruang.luas_bola(5)}")
print(f"Laus Tabung = {bangun_ruang.luas_tabung(5, 10)}")
print(f"Luas Kerucut = {bangun_ruang.luas_kerucut(5, 10)}")