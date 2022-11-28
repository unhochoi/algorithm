def solution(m, n, puddles):
    
    # 2차원 DP 테이블 초기화
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    # 시작 위치는 1로 처리
    dp[1][1] = 1
    
    # 웅덩이는 -1로 처리
    for i, j in puddles:
        dp[j][i] = -1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 시작 위치는 건너뛰기
            if (i == 1 and j == 1):
                continue
            # 현재 위치가 웅덩이라면
            if (dp[i][j] == -1):
                dp[i][j] = 0
            # 현재 위치가 웅덩이가 아니라면
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    
    return dp[n][m] % 1000000007