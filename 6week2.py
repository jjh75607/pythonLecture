for i in range(9, 1, -1):
    print("# %6d단 # " % i, end=" ")

print("\n")

for i in range(9, 0, -1):
    for j in range(9, 1, -1):
        print("%2dX  %2d=%2d   " % (j, i, i * j), end="")
    print("\n")
