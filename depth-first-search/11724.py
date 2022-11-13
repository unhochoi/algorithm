import sys
sys.setrecursionlimit(10**6)

# 정점의 개수 N과 간선의 개수 M
n, m = map(int, sys.stdin.readline().split())

# 간선 정보를 양방향으로 저장
graph = [[] for _ in range(n+1)]

# 각 노드가 어떤 그룹에 속해있는지 저장
group = [-1] * (n+1)

# 그룹 수
count = 1

# 간선 정보를 양방향으로 저장
for _ in range(m):
    
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

# node와 연결된 노드 탐색
def dfs(node):

    for neighbor in graph[node]:
        
        # 연결된 노드가 속한 그룹이 없다면
        if (group[neighbor] == -1):
            
            # node와 연결된 노드들을 모두 같은 그룹으로 처리
            group[neighbor] = group[node]
            
            # 연결된 노드들을 기준으로 dfs 반복
            dfs(neighbor)


# 1번 노드부터 마지막 노드까지 순서대로 탐색하며
# 현재 노드와 연결된 노드들을 모두 같은 그룹으로 처리
for i in range(1, n+1):

    # 현재 노드가 어떤 그룹에도 속해 있지 않은 경우, 해당 노드를 새로운 그룹으로 할당
    if (group[i] == -1):
        group[i] = count
        count += 1
        dfs(i)


# # 연결된 요소의 개수 출력
print(count-1)





