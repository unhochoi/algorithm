import sys

# 격자의 행의 수 n과 열의 수 m, ○로 표시된 칸의 번호
n, m, k = map(int, sys.stdin.readline().split())

# 경로 저장용 DP 테이블
graph = [[0]*m for _ in range(n)]

# 경로 결과
result = 1

# ○로 표시된 칸이 없다면
if (k == 0):
    # 1번 칸부터 NxM번 칸의 경로 탐색
    for i in range(n):
        for j in range(m):
            # 첫 행 및 첫 열이라면 경로를 1로 할당
            if (i==0 or j==0):
                graph[i][j] = 1
            # 나머지는 왼쪽 칸과 위쪽 칸의 덧셈 결과로 경로를 할당
            else:
                graph[i][j] = graph[i][j-1] + graph[i-1][j]
    
    # 경로 결과
    result *= graph[n-1][m-1]

# ○로 표시된 칸이 있다면
else:
    # 중간지점
    middle_x = (k-1) // m
    middle_y = (k-1) % m

    # 1번 칸부터 중간 지점까지의 경로 탐색
    for i in range(middle_x + 1):
        for j in range(middle_y + 1):
            # 첫 행 및 첫 열이라면 경로를 1로 할당
            if (i==0 or j==0):
                graph[i][j] = 1
            # 나머지는 왼쪽 칸과 위쪽 칸의 덧셈 결과로 경로를 할당
            else:
                graph[i][j] = graph[i][j-1] + graph[i-1][j]

    # 1번 칸부터 중간 지점까지의 경로 탐색 결과
    result *= graph[middle_x][middle_y]

    # 중간 지점부터 NxM번 칸까지의 경로 탐색
    for i in range(middle_x, n):
        for j in range(middle_y, m):
            # 중간 지점의 행 및 열 경로를 1로 할당
            if (i==middle_x or j==middle_y):
                graph[i][j] = 1
            # 나머지는 왼쪽 칸과 위쪽 칸의 덧셈 결과로 경로를 할당
            else:
                graph[i][j] = graph[i][j-1] + graph[i-1][j]
    
    # 경로 결과
    result *= graph[n-1][m-1]

print(result)