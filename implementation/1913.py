import sys

# 자연수 N 입력
n = int(sys.stdin.readline())

# 찾고자하는 자연수 입력
find = int(sys.stdin.readline())

# 결과 그래프
graph = [[0]*(n) for _ in range(n)]

# 상하좌우 이동 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 현재 시작 좌표 (중심점)
x, y = n//2, n//2
# 중심점에 번호 할당
graph[x][y] = 1

# 시작 번호
num = 2
# 시작 외각 크기
size = 3

# 현재 좌표가 표를 다 돌아, 0, 0이 될때까지
while (x != 0 or y != 0):

    # 번호가 현재 외각의 크기만큼 할당될때까지
    while (num <= size * size):

        # 현재 좌표가 현재 외각의 시작 좌표라면, 상으로 이동
        if (x == y == (n//2)):
            # 상우하좌로 이동해야하는 횟수 저장
            up, right, down, left = size, size-2, size-1, size-1
            # 상으로 이동
            x += dx[0]
            y += dy[0]
            # 상으로 이동해야하는 횟수 감소
            up -= 1

        # 우하좌상 이동 횟수가 남아있다면 이동
        elif (right > 0):
            x += dx[3]
            y += dy[3]
            right -= 1
        elif (down > 0):
            x += dx[1]
            y += dy[1]
            down -= 1
        elif (left > 0):
            x += dx[2]
            y += dy[2]
            left -= 1
        else:
            x += dx[0]
            y += dy[0]
            up -= 1

        # 현재 좌표에 번호 할당
        graph[x][y] = num
        num += 1
    
    # 현재 외각에 대한 번호 할당이 끝났으므로, 
    # 외각의 크기를 변경하고
    size += 2
    # 시작 좌표 변경을 위해 n 수정
    n -= 2

# 찾고자하는 값의 위치
find_x, find_y = -1, -1

# N개의 줄에 걸쳐 표를 출력
for i in range(len(graph)):
    for j in range(len(graph)):
        if (graph[i][j] == find):
            find_x, find_y = i, j
        print(graph[i][j], end = " ")
    print("")

# 찾고자하는 값의 위치 출력
print(find_x + 1, find_y + 1)
