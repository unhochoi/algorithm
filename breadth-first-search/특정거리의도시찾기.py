import sys
from collections import deque

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, sys.stdin.readline().split())

# 도시 생성
city = [[] for _ in range(n+1)]

# 최단 거리를 저장하기 위한 1차원 배열 생성
short_path = [-1]*(n+1)
# x의 거리는 0으로 지정
short_path[x] = 0

# 도로 입력 받기
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    city[i].append(j)

# BFS를 위한 큐 생성
q = deque()

# x부터 BFS 탐색 시작
def solution(x):

    # x를 큐에 삽입
    q.append(x)

    while (q):
        
        # 큐에서 원소 추출
        now = q.popleft()

        # 추출 도시의 이웃 도시 탐색
        for neighbor in city[now]:
            # 아직 방문하지 않은 도시라면
            if (short_path[neighbor] == -1):
                # 최단 거리 업데이트   
                # 방문한 도시는 무조건 최단 거리이므로, 방문하지 않은 도시에 대해서만 업데이트하면 됨
                short_path[neighbor] = short_path[now] + 1
                # 큐에 이웃 도시 추가
                q.append(neighbor)

    # 최단 거리 리스트에서, 거리가 k인 도시를 오름차순 출력
    # 숫자가 작은 도시부터 탐색하므로, 추가적인 정렬은 필요 없음
    find = False
    for i in range(1, len(short_path)):
        if (short_path[i] == k):
            print(i)
            find = True
    
    # 만약 최단 거리가 k인 도시가 없다면, -1 출력
    if (find == False):
        print(-1)

# 함수 호출
solution(x)


