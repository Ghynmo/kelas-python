listAngka = [2,3,10,6,4,8,1,"ayam","sapi","paimon"]
# print(listAngka[0])
# print(listAngka[1])
# print(listAngka[2])
# mengakses array
print(listAngka[-3])

print("=======LV1======")
# Perulangan(Loop) Level1
for i in range(3): # i dari (0-2)   0,1,2
    print(i) # i = 0

    # 2,3,10


print("=======LV2======")
# Perulangan(Loop) Level2
for i in range(2, 7): # i dari (2-3)
    print(listAngka[i])
    # 10,6


print("=======LV3======")
# Perulangan(Loop) Level3
for i in range(len(listAngka)): # i dari (total panjang listAngka)
    print(listAngka[i])
    # 2,3,10,6,4,8,1


print("=======LV4======")
# Perulangan(Loop) Level3
for i in range(2, len(listAngka)-2): # i dari (total panjang listAngka)
    print(listAngka[i])
    # 10,6,4,8,1