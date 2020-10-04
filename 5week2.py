n = int(input("숫자를 입력하세요 >>"))
re = 1

for i in range(2, n):
    if n % i == 0:
        re = 0

if not re:
    print("%d는 소수가 아닙니다" % n)
else :
    print("%d는 소수 입니다." % n)