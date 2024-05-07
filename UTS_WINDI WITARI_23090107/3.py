print("Jumlah Barang HARUS SESUAI dengan Jumlah Harga yang di Masukkan")
jumlah = int(input("Masukkan Jumlah Barang :"))
Harga = int(input("Masukkan Harga Barang :"))
pilihan = str(input("Apakah Ada barang tambahan(Y/N) :"))
Total1 = pilihan*Harga
Total = Total1*jumlah

if pilihan == 'Y':
        print(Harga)
else:
        print(Total)