import sys

# 특정 원소가 속한 집합을 찾기
def find(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if (parent[x] != x):
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(parent, x, y):
    a = find(parent, x)
    b = find(parent, y)
    if (a < b):
        parent[b] = a
    else:
        parent[a] = b

# 집의 수 n과 도로의 수 m 입력
n, m = map(int, sys.stdin.readline().split())
# 부모 테이블 초기화
parent = [i for i in range(n+1)]

# 모든 간선의 합
total = 0
# 모든 간선에 대한 정보를 입력받기
edge_array = []
for _ in range(m):    
    x, y, z = map(int, sys.stdin.readline().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    # (비용, 어디서부터, 어디로)
    edge_array.append((z, x, y))
    total += z

# 간선을 비용순으로 정렬
edge_array.sort()

# 최소 비용
result = 0

# 간선을 하나씩 확인하며
for cost, x, y in edge_array: 

    # 각 노드의 부모를 확인해, 사이클이 발생하지 않는 경우에만 집합에 포함
    if (find(parent, x) != find(parent, y)):
    
        union(parent, x, y)
        result += cost

print(total - result)
