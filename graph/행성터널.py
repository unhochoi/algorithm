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

# 행성의 개수 n
n = int(sys.stdin.readline())

# 특정 축 기준으로 저장한 뒤, 정렬
# (좌표 값, 행성 번호)
x = []
y = []
z = []
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))
x.sort()
y.sort()
z.sort()

# 특정 축 기준으로 모든 간선의 정보를 저장한 뒤, 정렬
# (특정 축 기준 양쪽 행성의 거리, 왼쪽 행성, 오른쪽 행성)
edges = []
for i in range(n-1):
    edges.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))
edges.sort()

# 부모 배열 초기화
parent = [i for i in range(n+1)]

# 최소 비용
result = 0

# 모든 간선 탐색
for cost, x, y in edges:

    # 해당 간선의 두 노드가 같은 사이클이 아니라면
    if (find(parent, x) != find(parent, y)):
        union(parent, x, y)
        result += cost

print(result)