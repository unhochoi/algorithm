# PyPy3로 제출

import sys

# 각각의 문자열
first = sys.stdin.readline().rstrip()
second = sys.stdin.readline().rstrip()

# DP 테이블
dp = [[0] * (len(second)) for _ in range(len(first))]

# 두 문자열에 모두 포함 된 부분 문자열 중 가장 긴 것의 길이
max_value = 0

# DP 진행
for i in range(len(first)):
    for j in range(len(second)):
        # 각각의 문자가 같다면
        if (first[i] == second[j]):
            # 첫 행이거나 첫 열이라면
            if (i == 0 or j == 0):
                dp[i][j] = 1
            # 나머지의 경우
            else:
                dp[i][j] = dp[i-1][j-1] + 1

            # 두 문자열에 모두 포함 된 부분 문자열 중 가장 긴 것의 길이
            max_value = max(max_value, dp[i][j])

print(max_value)
