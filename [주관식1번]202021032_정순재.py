num = int(input("input value : "))

for i in range(1, num + 1):
    if (i % 3 == 0) and (i % 7 == 0):
        print(i)