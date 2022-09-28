import sys
import heapq

# 테스트 케이스의 수
t = int(sys.stdin.readline())

# 상하좌우 확인용 인덱스
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 전체 테스트 케이스(Test Case)만큼 반복
for _ in range(t):

    # 탐사 공간의 크기
    n = int(sys.stdin.readline())

    # 탐사 공간 초기화
    graph = []
    for _ in range(n):
        # 각 칸의 비용 입력
        graph.append(list(map(int, sys.stdin.readline().split())))

    # 최단 경로 초기화
    shortest_path = [[int(1e9)] * n for _ in range(n)]

    # 시작 노드의 최단 경로 표시
    shortest_path[0][0] = graph[0][0]

    # 최소 비용을 가지는 노드를 선택하기 위한 우선순위 큐 선언 (비용, x좌표, y좌표)
    hq = []
    
    # 큐에 시작 노드를 삽입
    heapq.heappush(hq, (graph[0][0], 0, 0))

    # 다익스트라 알고리즘을 수행
    while hq:

        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        now_cost, now_x, now_y = heapq.heappop(hq)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if (now_cost > shortest_path[now_x][now_y]):
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in range(4):
            # 인접한 노드의 위치
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            # 인접한 노드에 접근 가능하다면
            if (0 <= nx < n and 0 <= ny < n):
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if (shortest_path[nx][ny] > now_cost + graph[nx][ny]):
                    shortest_path[nx][ny] = now_cost + graph[nx][ny]
                    heapq.heappush(hq, (shortest_path[nx][ny], nx, ny))

    print(shortest_path[n-1][n-1])

