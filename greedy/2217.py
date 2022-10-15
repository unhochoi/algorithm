import sys

n = int(sys.stdin.readline())

arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

# 내림차순 정렬
arr.sort(reverse=True)

# 가장 큰 값부터 (값 x 확인한 값의 개수)를 계산하며 가장 큰 값을 저장
result = 0
for i in range(n):
    result = max(result, arr[i] * (i+1))

print(result)