start = int(input("첫 번째 숫자를 입력하세요 >>"))
end = int(input("두 번째 숫자를 입력하세요 >>"))
t = int(input("더할 숫자를 입력하세요 >>"))

sum = 0

for i in range(start, end + 1, t):
    sum += i

print("%d %d ...... %d는    %d" % (start, start + t, end, sum))
