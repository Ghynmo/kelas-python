def SelisihMaksimum(listAngka):    
    # Menyimpan selisih terbesar
    selisih_terbesar = 0
    # Menyimpan dua angka yang menghasilkan selisih terbesar
    angka_kecil = 0
    angka_besar = 0
    
    # Contoh: listAngka = [2,3,10,6,4,8,1]
    [2,3,10,6,4,8,1]
    [2,3,10,6,4,8,1]
    10 paling besar setlah angka paling kecil


    # Loop pertama untuk angka yang lebih kecil
    for i in range(len(listAngka)): # i dari (total panjang listAngka) = 7x loop
        print("perulangan ke ", i)
        # i0 = 2,  i1 = 3,  i2 = 10,  i3 = 6,  i4 = 4, i5 = 8,  i6 = 1

        for j in range(i+1, len(listAngka)):
            # i0 = 3,10,6,4,8,1
            # i1 = 10,6,4,8,1
            # i2 = 6,4,8,1
            # i3 = 4,8,1
            # i4 = 8,1
            # i5 = 1
            # i6 = 

            if numbers[j] > numbers[i]:
                # Hitung selisih antara dua angka
                selisih = listAngka[j] - listAngka[i]
                # selisih = abs(selisih)

                print("             selisih = ", selisih)
                
                # Jika selisih yang baru lebih besar, simpan
                if selisih > selisih_terbesar:
                    selisih_terbesar = selisih
                    angka_i = listAngka[i]
                    angka_j = listAngka[j]
    
    # Tampilkan hasil
    print(f"Selisih maksimum: {selisih_terbesar} (dari {angka_besar} - {angka_kecil})")



# Minta input dari pengguna
input_string = input("Masukkan angka (pisahkan dengan koma). Contoh: 2,3,10,6,4,8,1\n")

# Ubah input string menjadi list angka
listAngka = [int(x) for x in input_string.split(',')]

# Panggil fungsi untuk mencari selisih maksimum
SelisihMaksimum(listAngka)