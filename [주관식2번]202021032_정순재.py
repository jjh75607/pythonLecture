def measure(a, x):
    if a % x == 0:
        print(x)
    if x == a:
        return 0
    measure(a, x + 1)


n = int(input("약수 입력 : "))
measure(n, 1)
