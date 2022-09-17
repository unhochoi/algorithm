import sys

# 집의 수
n = int(sys.stdin.readline())

# 집의 위치
pos = list(map(int, sys.stdin.readline().split()))

# 집의 위치 정렬
pos.sort()

# 집이 짝수개라면
if (len(pos)%2 == 0):
    print(pos[len(pos)//2-1])
# 집이 홀수개라면
if (len(pos)%2 == 1):
    print(pos[len(pos)//2])
