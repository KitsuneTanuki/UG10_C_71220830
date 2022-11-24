print("========== Pilih menu ==========")
print("1. Tambah")
print("2. Kurang")
print("3. Kali")
print("4. Bagi")
angka1 = eval(input("Masukkan angka pertama: "))
angka2 = eval(input("Masukkan angka kedua: "))

Pilihan = input("Pilihan Anda: ")
if Pilihan == "1":
    print(angka1 + angka2)
elif Pilihan == "2":
    print(angka1 - angka2)
elif Pilihan == "3":
    print(angka1 * angka2)
elif Pilihan == "4":
    print(angka1 / angka2)
else:
    print("error")
