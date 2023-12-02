import sys

n, k = map(int, sys.stdin.readline().split())

coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for j in range(coin, k+1):
        dp[j] = dp[j] + dp[j-coin]

print(dp[k])