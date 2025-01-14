listAngka = [2,3,10,6,4,8,1]

print("=======LV1======")
# Perulangan bersarang (nested-Loop) Level1
for i in range(len(listAngka)): # i dari (total panjang listAngka) = 7x loop
    # 2,3,10,6,4,8,1
    print("perulangan ke ", i)

    for j in range(len(listAngka)):
    # 2,3,10,6,4,8,1
        print("i = ", listAngka[i], " j = ", listAngka[j])




print("=======LV2======")
# Perulangan bersarang (nested-Loop) Level2
for i in range(4, len(listAngka)-1): # i dari (total panjang listAngka) = 7x loop
    # 4,8
    print("perulangan ke ", i)

    for j in range(2, len(listAngka)):
    # 10,6,4,8,1
        print("i = ", listAngka[i], " j = ", listAngka[j])



print("=======LV3======")
# Perulangan bersarang (nested-Loop) Level3
for i in range(len(listAngka)): # i dari (total panjang listAngka) = 7x loop
    print("perulangan ke ", i)
    # i = 0-6

    for j in range(i+1, len(listAngka)):
        # i0 = 3,10,6,4,8,1  (1-7)
        # i1 = 10,6,4,8,1    (2-7)
        # i2 = 6,4,8,1       (3-7)
        # i3 = 4,8,1
        # i4 = 8,1
        # i5 = 1
        # i6 = 

        print("i = ", listAngka[i], " j = ", listAngka[j])


# ********
# *******
# ******
# *****
# ****
# ***
# **
# *


