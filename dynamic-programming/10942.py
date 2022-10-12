import sys

# 수열의 크기 N
n = int(sys.stdin.readline())
# 칠판에 적은 수 N개
array = list(map(int, sys.stdin.readline().split()))
# 각 숫자간의 팰린트롬 정보를 저장하는 DP 테이블
dp = [[0] * n for _ in range(n)]

# 연속된 숫자가 1개일 경우
for i in range(n):
    dp[i][i] = 1

# 연속된 숫자가 2개일 경우
for i in range(n-1):
    # 양끝 숫자가 같다면
    if (array[i] == array[i+1]):
        dp[i][i+1] = 1
    # 양끝 숫자가 다르다면
    else:
        dp[i][i+1] = 0

# 연속된 숫자가 3개 이상일 경우

# 연속된 숫자의 개수
for continue_number in range(3, n+1):
    # 첫 인덱스
    for start in range(n - continue_number + 1):
        # 마지막 인덱스
        end = start + continue_number - 1
        
        # 양끝 숫자가 같고, 그 사이의 숫자들이 팰린드롬이라면
        if (array[start] == array[end] and dp[start+1][end-1] == 1):
            dp[start][end] = 1

# 질문의 개수 M
m = int(sys.stdin.readline())

# 각 질문
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())

    # 팰린드롬 결과 출력
    print(dp[s-1][e-1])
