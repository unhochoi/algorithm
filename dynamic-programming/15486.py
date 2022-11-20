import sys

n = int(sys.stdin.readline())

t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액

# i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
dp = [0] * (n+1)

for _ in range(n):

    # 날짜별 상담 완료 기간 및 상담 완료 금액 저장
    x, y = map(int, sys.stdin.readline().split(" "))
    t.append(x)
    p.append(y)

# i번째 날부터 마지막 날까지 낼 수 있는 최대 이익
max_value = 0

# 마지막 날짜부터 역순으로 탐색
for i in range(n-1, -1, -1):
    
    # 해당 날짜에 상담을 진행할 수 있다면
    if (i + t[i] <= n):
        
        # [현재 상담 일자의 이윤 + 현재 상담을 마친 일자부터의 최대 이윤]과
        # 현재 날짜부터 마지막 날까지 낼 수 있는 최대 금액을 비교
        dp[i] = max(p[i] + dp[i + t[i]], max_value)
        max_value = dp[i]
    
    # 해당 날짜에 상담을 진행할 수 없다면
    else:
        dp[i] = max_value

print(max_value)


