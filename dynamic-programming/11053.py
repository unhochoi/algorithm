import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))

# dp 테이블 초기화
dp = [1] * n

for i in range(n):
    for j in range(i):
        # i번째 수보다 작은 수에 대해서
        if (arr[j] < arr[i]):
            # dp 테이블의 i번째 길이와 [dp 테이블의 j번째 길이 + 1]을 비교한 뒤, 최댓값을 dp[i]로 기록
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))