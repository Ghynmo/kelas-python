# Index array (mengakses nilai array)
listAngka = [2,3,10,6,4,8,1,"ayam","sapi","paimon"]

print("=======LV1======")
print(listAngka[7]) # Ayam

print("=======LV2======")
print(listAngka[-1]) # Paimon

print("=======LV3======")
print(listAngka[5:8]) # [8, 1, 'ayam']



listAngka = [2,3,10,6,4,8,1,"ayam","sapi","paimon"]

# Append array (menambah element kedalam array)
listAngka.append(10)
print(listAngka) # [2,3,10,6,4,8,1,"ayam","sapi","paimon",10]


# Remove array (menghapus element atau item)
listAngka.remove("sapi")
print(listAngka) # [2,3,10,6,4,8,1,"ayam","paimon",10]

listAngka.remove(10) 
print(listAngka) # [2,3,6,4,8,1,"ayam","paimon",10]
# yang dihapus hanya angka 10 di awal


# Pop array (menghapus berdasarkan index)
listAngka.pop() # menghapus index terakhir
print(listAngka) # [2,3,6,4,8,1,"ayam","paimon"]

listAngka.pop(3)
print(listAngka) # [2,3,6,8,1,"ayam","paimon"]