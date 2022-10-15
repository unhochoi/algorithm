import sys

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

result = 0
sum = 0
for num in arr:
    sum += num
    result += sum

print(result)

