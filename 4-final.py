def SelisihMaksimum(numbers):
    # Pastikan list memiliki minimal 2 angka
    if len(numbers) < 2:
        print("Error: Minimal harus ada 2 angka dalam list!")
        return
    
    # Menyimpan selisih terbesar
    selisih_terbesar = 0
    # Menyimpan dua angka yang menghasilkan selisih terbesar
    angka_kecil = 0
    angka_besar = 0
    
    # Contoh: numbers = 2,3,10,6,4,8,1

    # Loop pertama untuk angka yang lebih kecil
    for i in range(len(numbers)):
        # 7x
        # 2,3,10,6,4,8,1

        # Loop kedua untuk mencari angka yang lebih besar setelahnya
        for j in range(i + 1, len(numbers)):
            # i1 = 3,10,6,4,8,1
            # i2 = 10,6,4,8,1
            # i3 = 6,4,8,1
            # i4 = 4,8,1
            # i5 = 8,1
            # i6 = 1

            # Hanya hitung selisih jika angka kedua lebih besar
            if numbers[j] > numbers[i]:
                # Hitung selisih antara dua angka
                selisih = numbers[j] - numbers[i]
                
                # Jika selisih yang baru lebih besar, simpan
                if selisih > selisih_terbesar:
                    selisih_terbesar = selisih
                    angka_kecil = numbers[i]
                    angka_besar = numbers[j]
    
    # Tampilkan hasil
    print(f"Selisih maksimum: {selisih_terbesar} (dari {angka_besar} - {angka_kecil})")

# Program utama
print("Program Mencari Selisih Maksimum")
print("--------------------------------")

# Minta input dari pengguna
input_string = input("Masukkan angka (pisahkan dengan koma). Contoh: 2,3,10,6,4,8,1\n")

# Ubah input string menjadi list angka
numbers = [int(x) for x in input_string.split(',')]

# Panggil fungsi untuk mencari selisih maksimum
SelisihMaksimum(numbers)