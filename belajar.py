import random



nama = input("masukkan nama anda :")
posisi_hadiah = random.randint(1, 4)

print(f"halo {nama} coba perthatikan goa di bawah ini" )
print("|_| |_| |_| |_| ")
print("menurut kamu ada di nomer berapa hadiah berada?")
pilihan_user = input("menurut kamu ada di nomer berapa? 1/2/3/4")
print(f'pilihan kamu adalah: {pilihan_user}')

if pilihan_user == posisi_hadiah:
    print(f'selamat {user} kamu menang hadiah berada di {posisi_hadiah} dan pilihan mu adalah {pilihan_user} ')
else:c
    print(f'kamu kalah hadiah ada di nomor {posisi_hadiah}')