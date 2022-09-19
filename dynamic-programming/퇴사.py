import sys

# 전체 상담 개수
n = int(sys.stdin.readline())

t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액

dp = [0] * (n + 1) # i번째 날부터 마지막 날까지 낼 수 있는 최대 이익

max_value = 0

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1):

    # i번째 날짜에 상담이 가능한 경우
    if (i + t[i] <= n):
        # (현재 상담 날짜의 금액 + 다음 상담 날짜의 누적 금액)과
        # 현재 상담 날짜부터 마지막 날까지 쌓을 수 있는 최대 누적 금액을 비교
        dp[i] = max(p[i] + dp[i+t[i]], max_value)
        max_value = dp[i]
    # i번째 날짜에 상담이 불가능한 경우
    else:
        dp[i] = max_value

print(max_value)