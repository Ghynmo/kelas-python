listAngka = [2,3,10,6,4,8,1]
print("=======LV3======")
# Perulangan bersarang (nested-Loop) Level1
for i in range(len(listAngka)): # i dari (total panjang listAngka) = 7x loop
    print("perulangan ke ", i)
    # i0 = 2,  i1 = 3,  i2 = 10,  i3 = 6,  i4 = 4, i5 = 8,  i6 = 1

    for j in range(i+1, len(listAngka)):
        # i0 = 3,10,6,4,8,1  (1-7)
        # i1 = 10,6,4,8,1    (2-7)
        # i2 = 6,4,8,1       (3-7)
        # i3 = 4,8,1
        # i4 = 8,1
        # i5 = 1
        # i6 = 

        print("i = ", listAngka[i], " j = ", listAngka[j])
