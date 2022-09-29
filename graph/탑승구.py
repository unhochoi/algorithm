import sys

# 특정 원소가 속한 집합을 찾기
def find(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 탑승구의 수
g = int(sys.stdin.readline())

# 비행기의 수
p = int(sys.stdin.readline())

# 부모 테이블 초기화
parent = [i for i in range(g+1)]

# 도킹할 수 있는 비행기의 최대 개수
result = 0

for _ in range(p):
    
    # 비행기가 도킹할 수 있는 탑승구의 가장 큰 번호
    docking = int(sys.stdin.readline())

    # 해당 탑승구의 루트 노드
    root = find(parent, docking)

    # 루트 노드가 0이라면
    if (root == 0):
        break
    # 루트 노드가 0이 아니라면
    else:
        # 루트 노드와 루트 노드의 왼쪽 노드를 합집합
        union(parent, root, root-1)
        result += 1

print(result)





