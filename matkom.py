# soal 1
hasil = 0
n = 6
for i in range(3, n+1):
    hasil = hasil + i*i
print(hasil)

# soal 2
hasil = 0
n = 4
for i in range(1, n+1):
    hasil = hasil+(2*i)
print(hasil)

# soal 3
hasil = 1
n = 3
for i in range(1, n+1):
    hasil = hasil*i
print(hasil)

# soal 4
hasil = 0
n = 10
for i in range(1, n+1):
    hasil = hasil + i
print(hasil)

# soal 5
aldo_awal = 10_000_000
bunga = [0.05, 0.04, 0.06, 0.05]

faktor = 1
for r in bunga:
    faktor *= (1 + r)
saldo_akhir = saldo_awal * faktor

print(f"Saldo akhir setelah 4 tahun adalah Rp {saldo_akhir:,.2f}")



