satu = print(" BMI < 18.5 : Berat badan kurang")
dua = print("  18.5 <= BMI < 24.9 : Berat badan normal")
tiga = print(" 25 <= BMI <29.9 : Kelebihan Berat badan")
empat = print(" BMI >= 30 : Obesitas")

BB = int(input("Masukkan Berat Badan (Kg) :"))
TB = int(input("Masukkan Tinggi Badan (M) :"))
print("Tinggi Badan :", TB)
print("Berat Badan :", BB)
total = (TB*TB)
BMI = print("Hasil Perhitungan Berat Badan / Tinggi badan(kuadrat) :", BB/total)

if BMI < 18.5:
    print("Berat badan kurang")
elif 18.5 <= BMI < 24.9:
    print("Berat badan normal")
elif 25 <= BMI <29.9:
    print("Kelebihan Berat badan")
elif BMI >= 30:
    print("Obesitas")
else:
    print("Tidak Terdeteksi")
