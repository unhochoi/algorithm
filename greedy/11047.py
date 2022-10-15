import sys

# 동전의 종류 N과 가치의 합 K
n, k = map(int, sys.stdin.readline().rstrip().split())

# 동전 저장
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

# 동전의 개수
count = 0
for i in range(n-1, -1, -1):

    # 동전이 남은 금액보다 작거나 같다면
    if (arr[i] <= k):
        # 몫으로 사용된 동전의 개수를 추가
        count += k // arr[i] 
        # 남은 가치의 합
        k = k % arr[i]
    # 남은 가치의 합이 없다면
    if (k == 0):
        break

# 동전의 개수 출력
print(count)