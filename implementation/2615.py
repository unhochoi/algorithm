import sys

# 바둑판 초기화
board = []
for i in range(19):
    board.append(list(map(int, sys.stdin.readline().split())))

# 연속된 다섯 개의 바둑알 중 가장 왼쪽에 있는 바둑알의 좌표를 출력해야하므로, 4가지 방향으로 진행
# → ↓ ↘ ↗
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

# 바둑알을 찾았는지 여부
find = False

def solution():
    
    global find

    # 바둑판 탐색
    for x in range(19):
        for y in range(19):
            
            # 바둑알이 놓아져있다면
            if board[x][y] != 0:

                # 바둑알 번호
                focus = board[x][y]

                # 4가지 방향 탐색
                for i in range(4):
                    
                    cnt = 1

                    # 주위 바둑알의 위치
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 동일한 번호를 가진 바둑알이 주위에 있다면
                    while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == focus:
                        
                        cnt += 1

                        # 육목 체크
                        if cnt == 5:
                            
                            # 첫 바둑알을 놓은 방향 이전에 바둑알이 하나 더 있는지 확인
                            if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x - dx[i]][y - dy[i]] == focus:
                                break
                            # 마지막 바둑알을 놓은 방향 이후에 바둑알이 하나 더 있는지 확인
                            if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx + dx[i]][ny + dy[i]] == focus:
                                break
                            
                            # 육목이 아니라면 성공이므로 종료
                            print(focus)
                            print(x + 1, y + 1)
                            find = True

                            return 
                        
                        # 탐색 방향으로 위치 업데이트
                        nx += dx[i]
                        ny += dy[i]

    # 오목을 찾지 못했다면
    if (find == False):
        print(0)
        return

# 함수 호출
solution()