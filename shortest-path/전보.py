from dis import dis
from math import dist
import sys
import heapq

# N, M, C 입력 받기
n, m, c = map(int, sys.stdin.readline().rstrip().split())

# 그래프 초기화
graph = [[] for _ in range(n+1)]

# 최소 비용 배열 초기화
distance = [int(1e9)] * (n+1)

# 간선 초기화
for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append((end, cost))

# 다익스트라 함수 생성
def dijkstra(start):

    # 시작 노드 비용 초기화
    distance[start] = 0

    # 우선 순위 큐 생성
    q = []

    # 시작 노드를 우선 순위 큐에 삽입 (비용, 도착 노드)
    heapq.heappush(q, (0, start))

    # 우선 순위 큐 탐색
    while q:
        
        # 우선순위큐에서 최소 비용 노드 추출
        cost, now = heapq.heappop(q)
        
        # 시작 노드에서 추출한 노드까지의 비용이 
        # 시작 노드에서 추출 노드까지의 현재 비용보다 클 경우는 진행하지 않음
        if (cost > distance[now]):
            continue

        # 추출 노드와 인접한 노드 확인
        # neighbor = (도착 노드, 비용)
        for neighbor in graph[now]:
            
            # 시작 노드와 인접한 노드 간 기존 비용 vs 추출 노드를 거쳐갈 때의 비용
            if (distance[neighbor[0]] > cost + neighbor[1]):
                # 최소 비용 배열 업데이트
                distance[neighbor[0]] = cost + neighbor[1]
                # 우선순위큐에 업데이트 내용 삽입
                heapq.heappush(q, (cost + neighbor[1], neighbor[0]))

# 다익스트라 실행
dijkstra(c)

# 도시 C에서 보낸 메세지를 받게 되는 도시의 개수
count = 0
# 도시 C에서 보낸 메시지를 받을 수 있는 도시들이 모두 메시지를 받는 데까지 걸리는 시간
max = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if (d < int(1e9)):
        count += 1
        if (d > max):
            max = d

# 시작 노드는 제거해야 하므로 count - 1을 출력
print(count - 1 , max)

