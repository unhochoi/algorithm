import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))

# dp 테이블 초기화
dp = [x for x in arr]

for i in range(n):
    for j in range(i):
        # i번째 수보다 작은 수에 대해서
        if (arr[j] < arr[i]):
            # dp 테이블의 i번째 값과 [dp 테이블의 j번째 값 + i번째 원소의 값]을 비교한 뒤,
            # 최댓값을 dp[i]로 기록
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))