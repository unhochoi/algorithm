import sys

# 여행지가 속한 집합 찾기
def find(parent, x):
    # 해당 여행지가 루트 집합이 아니라면, 루트 집합 찾기
    if (parent[x] != x):
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 여행지가 속한 집합을 합치기
def union(parent, x, y):
    a = find(parent, x)
    b = find(parent, y)
    if (a < b):
        parent[b] = a
    else:
        parent[a] = b

# 여행지의 수 n과 여행 계획에 속한 도시의 수 m
n, m = map(int, sys.stdin.readline().split())
# 각 여행지가 속한 집합을 저장하기 위한 1차원 배열
parent = [i for i in range(n+1)]

# 여행지 연결 정보
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        # 해당 여행지가 연결되어 있다면
        if (row[j] == 1):
            # 간선 정보에 따라 합집합 진행
            union(parent, i, j)

# 여행지 계획
plan = list(map(int, sys.stdin.readline().split()))

# 여행 계획에 속하는 모든 노드의 루트가 동일한지 확인
result = True
for i in range(m - 1):
    if find(parent, plan[i]) != find(parent, plan[i + 1]):
        result = False
        break

# 여행 경로의 노드가 같은 모두 집합인지 확인
if (result == True):
    print('YES')
else:
    print('NO')