pesanan = input("Masukkan daftar pesanan : ")
t = pesanan.split(", ")
print("Daftar pesanan :",t)
u = input("Masukkan pesanan yang ingin ditambahkan : ")

if u not in t:
    t.append(u)
    print("Hasil penambahan pada daftar pesanan :",t)
else:
    print(u.capitalize(), "sudah berada dalam daftar pesanan.")
