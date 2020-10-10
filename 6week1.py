
for i in range(10):
    if i < 5:
        for k in range(4 - i):
            print('   ', end='')
        for k in range(i * 2 + 1):
            print("\u2665", end='')
    else:
        for k in range(i - 4):
            print('   ', end='')
        for k in range((9 - i) * 2 - 1):
            print("\u2665", end='')
    print()