import sys

n = int(sys.stdin.readline())

# dp 테이블
dp = [0] * 1001

# 초기값 설정
dp[1] = 1
dp[2] = 2

# bottom-up 진행
for i in range(3, n+1):
   dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)