hard = int(input("Введите число: "))
passport_ = []
for i in range(1,hard):
    for j in range(i,hard):
        if hard % (i+j) == 0 :
            passport_.append(str(i)+"+"+str(j))
print(hard," - ",passport_)