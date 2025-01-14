from array import array

def HapusDuplikatNumber(numbers):
    # Membuat list kosong untuk menyimpan angka-angka unik
    hasil = [] #4,2,5,
    
    # Periksa setiap angka dalam input
    for angka in numbers:
        # Jika angka belum ada dalam list hasil, tambahkan
        if angka not in hasil:
            hasil.append(angka)
    
    return hasil


# Masukkan list angka
input_angka = input("Masukkan angka (contoh: [4,2,5,2,3,5,1,4]): ")
# string "[4,2,5,2,3,5,1,4]"

# Ubah string input menjadi list
list_angka = eval(input_angka)
# list [4,2,5,2,3,5,1,4]

# Ubah list menjadi array
array_angka = array('i', list_angka)
# array [4,2,5,2,3,5,1,4]


hasil_akhir = HapusDuplikatNumber(array_angka)


# Tampilkan hasil
print("\nList tanpa duplikat:", hasil_akhir)