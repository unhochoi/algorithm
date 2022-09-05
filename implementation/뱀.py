import sys

# 보드의 크기
n = int(sys.stdin.readline())

# 보드 생성
board = [[0]*n for _ in range(n)]

# 사과의 개수
k = int(sys.stdin.readline())
# 사과의 위치
for _ in range(k):
    i, j = map(int, sys.stdin.readline().split())
    board[i-1][j-1] = 1

# 뱀의 방향 변환 횟수
l = int(sys.stdin.readline())
# 뱀의 방향 변환 정보
rotate = []
for _ in range(l):
    x, c = sys.stdin.readline().split()
    rotate.append((int(x), c))

# 방향 전환 인덱스 (동남서북)
# 오른쪽 방향 전환 'D' 시 인덱스 증가, 왼쪽 방향 전환 'L' 시 인덱스 감소
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def simulate():
    # 시작 위치
    i, j = 0, 0
    # 뱀의 시작 위치 저장
    board[i][j] = 2
    # 현재 방향
    dir = 0
    # 초과 시간
    time = 0
    # 뱀의 몸 위치를 저장
    snake = [(0,0)]

    while True:
        
        # 다음 위치
        new_x = i + dx[dir]
        new_y = j + dy[dir]

        # 다음 위치에 뱀이 벽에 부딪히거나, 뱀의 몸에 부딪히는지 확인
        if (0 > new_x or new_x >= n or 0 > new_y or new_y >= n or board[new_x][new_y] == 2 ):
            time += 1
            break
        
        # 다음 위치로 이동할 수 있다면
        else:
            # 다음 위치가 사과라면
            if (board[new_x][new_y] == 1):
                # 뱀 머리 위치 표시
                board[new_x][new_y] = 2
                # 뱀 머리 위치 저장
                snake.append((new_x, new_y))
            
            # 다음 위치가 사과가 아니라면
            else:
                # 뱀 머리 위치 표시
                snake.append((new_x, new_y))
                # 뱀 머리 위치 저장
                board[new_x][new_y] = 2
                # 뱀 꼬리 위치 저장 제거
                px, py = snake.pop(0)
                # 뱀 꼬리 위치 표시 제거
                board[px][py] = 0

        # 현재 위치 변경
        i, j = new_x, new_y
        # 시간 증가
        time += 1

        # 방향 전환이 남아있으며, 다음 차례가 방향 전환 시간이라면
        if (len(rotate) >= 1 and time == rotate[0][0]):
            # 오른쪽 방향 전환이라면
            if (rotate[0][1] == 'D'):
                dir = (dir + 1) % 4
            # 왼쪽 방향 전환이라면
            else:
                dir = (dir - 1) % 4
            
            #  방향 전환했으므로 리스트에서 제거
            rotate.pop(0)
        
    return time

print(simulate())

