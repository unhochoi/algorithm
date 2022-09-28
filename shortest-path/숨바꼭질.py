import sys
import heapq

# 헛간의 개수 n과 양방향 통로의 개수 m
n, m = map(int, sys.stdin.readline().split())

# 헛간 통로 정보 초기화
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # 양방향 통로 추가
    graph[a].append((b, 1))
    graph[b].append((a, 1))

# 1차원 최단 거리 배열 초기화
shortest_path = [int(1e9)] * (n+1)

# 우선순위 큐 초기화 (비용, 도착지)
hq = []
heapq.heappush(hq, (0, 1))

# 시작점의 최단 거리 초기화
shortest_path[1] = 0

# 다익스트라 탐색
while hq:

    # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
    now_cost, now = heapq.heappop(hq)

    # 새로 추출한 현재 노드까지의 최단 거리보다 
    # 기존의 현재 노드까지의 최단 거리가 짧을 경우 무시
    if (now_cost > shortest_path[now]):
        continue

    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for next, next_cost in graph[now]:
        # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
        if (shortest_path[next] > now_cost + next_cost):
            shortest_path[next] = now_cost + next_cost
            heapq.heappush(hq, (shortest_path[next], next))

# 가장 최단 거리가 먼 노드 번호(동빈이가 숨을 헛간의 번호)
result = -1

# 도달할 수 있는 노드 중에서, 가장 최단 거리가 먼 노드와의 최단 거리
max = -int(1e9)

# 가장 최단 거리가 먼 노드와 동일한 최단 거리를 가지는 노드의 개수
count = 0

for i in range(1, n+1):
    if (max < shortest_path[i]):
        result = i
        max = shortest_path[i]
        count = 0
    if (max == shortest_path[i]):
        count += 1

print(result, max, count)


        
