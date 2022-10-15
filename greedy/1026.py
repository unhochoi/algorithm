import sys

# 정수의 개수
n = int(sys.stdin.readline())

first = list(map(int, sys.stdin.readline().split()))
second = list(map(int, sys.stdin.readline().split()))

first.sort()
second.sort(reverse=True)

result = 0

for i in range(n):
    result += first[i] * second[i]

print(result)