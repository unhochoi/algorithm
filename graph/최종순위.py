import sys
from collections import deque

# 테스트 케이스의 개수 
tc = int(sys.stdin.readline())

for _ in range(tc):

    # 팀의 수 n
    n = int(sys.stdin.readline())

    # 각 노드의 진입차수 초기화
    indegree = [0] * (n+1)

    # 각 노드에 연결된 간선 정보를 담기 위한 인접 행렬 초기화
    # [큰 순위의 팀 번호][작은 순위의 팀번호] = True
    graph = [[False] * (n + 1) for i in range(n + 1)]

    # 작년 팀 등수 (인덱스 == 등수, 값 == 팀 번호)
    t = list(map(int, sys.stdin.readline().split()))

    # 방향 그래프의 간선 정보 초기화
    for i in range(n):
        for j in range(i + 1, n):
            # [큰 순위의 팀 번호][작은 순위의 팀번호] = True
            graph[t[i]][t[j]] = True
            # 진입 차수 추가
            indegree[t[j]] += 1

    # 올해 변경된 순위 정보 입력
    m = int(sys.stdin.readline())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        
        # a, b가 큰 순위의 팀번호, 작은 순위의 팀 번호라면
        if (graph[a][b]):
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        # 반대라면
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1
    
    # 위상 정렬(Topology Sort) 시작
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 진입 차수가 0인 노드를 찾아 큐에 삽입
    for i in range(1, n+1):
        if (indegree[i] == 0):
            # 큐에 팀 번호 삽입
            q.append(i)
    
    cycle = False # 데이터에 일관성이 없어서 순위를 정할 수 없는 경우 == 사이클이 발생하는 경우 == 노드가 N번 나오기 전에 큐가 비게 되는 경우
    certain = True # 확실한 순위를 찾을 수 없는 경우 == 특정 시점에 2개 이상의 노드가 큐에 한꺼번에 들어가는 경우
    
    # 정확히 노드의 개수만큼 반복
    for i in range(n):
        # 큐가 비어 있다면 사이클이 발생했다는 의미
        if len(q) == 0:
            cycle = True
            break
        # 큐의 원소가 2개 이상이라면 가능한 정렬 결과가 여러 개라는 의미
        if len(q) >= 2:
            certain = False
            break
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 결과 리스트에 추가
        result.append(now)

        # 해당 노드와 연결된 노드들의 진입 차수 빼기
        for j in range(1, n+1):
            if (graph[now][j] == True):
                indegree[j] -= 1
                # 새롭게 진입 차수가 0이 된 노드를 찾아 큐에 삽입
                if (indegree[j] == 0):
                    q.append(j)
        
    # 사이클이 발생하는 경우(일관성이 없는 경우)
    if cycle == True:
        print("IMPOSSIBLE")
    # 위상 정렬 결과가 여러 개인 경우
    elif certain == False:
        print("?")
    # 위상 정렬을 수행한 결과 출력
    else:
        for i in result:
            print(i, end=' ')
        print()


