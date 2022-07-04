import sys

# N, M 입력
n, m = map(int, sys.stdin.readline().rstrip().split())

# 그래프 초기화
graph = [[int(1e9)] * (n+1) for _ in range(n+1)]

# 그래프 대각선 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 양방향 간선 추가
for _ in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    graph[start][end] = 1
    graph[end][start] = 1

# X, K 입력
x, k = map(int, sys.stdin.readline().rstrip().split())

# 플로이드 워셜 알고리즘 실행
for i in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

# [1번 노드에서 K 노드로 가는 최소 비용 + K 노드에서 X 노드로 가는 최소 비용] 출력

# 도달할 수 있을 경우
if (graph[1][k] + graph[k][x] < int(1e9)):
    print(graph[1][k] + graph[k][x])
# 도달할 수 없을 경우
else:
    print(-1)
