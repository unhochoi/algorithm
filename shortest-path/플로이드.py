import sys

# 도시의 개수 n과 버스의 개수 m 입력
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

# 그래프 정보 저장
graph = [[int(1e9)]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, sys.stdin.readline().split())
    # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있으므로
    # 가장 짧은 간선 정보만 저장
    if c < graph[a][b]:
        graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 수행된 결과를 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        # 도달할 수 없는 경우, 0을 출력
        if (graph[i][j] == int(1e9)):
            print(0, end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[i][j], end=" ")
    print()