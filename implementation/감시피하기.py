import sys
from itertools import combinations

# 복도 크기 입력
n = int(sys.stdin.readline())
# 복도 정보
hallway = []
# 선생님 위치
teachers = []
# 빈칸 위치
emptys = []

# 복도 정보 입력
for i in range(n):
    
    row = sys.stdin.readline().split()
    hallway.append(row)
    
    for j in range(n):
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if (row[j] == 'X'):
            emptys.append((i, j)) 
        # 선생님이 존재하는 위치 저장
        elif (row[j] == 'T'):
            teachers.append((i, j)) 

# 선생님의 위치 x, y를 기준으로 direction 방향으로 감시를 진행 (학생 발견 : True, 학생 미발견 : False)
def watch(x, y, direction):
    if direction == 0: #동쪽
        while (y < n):
            if (hallway[x][y] == 'O'): # 장애물이 있는 경우
                return False
            if (hallway[x][y] == 'S'): # 학생이 있는 경우
                return True
            y += 1
    if direction == 1: #서쪽
        while (y >= 0):
            if (hallway[x][y] == 'O'): # 장애물이 있는 경우
                return False
            if (hallway[x][y] == 'S'): # 학생이 있는 경우
                return True
            y -= 1
    if direction == 2: #남쪽
        while (x < n):
            if (hallway[x][y] == 'O'): # 장애물이 있는 경우
                return False
            if (hallway[x][y] == 'S'): # 학생이 있는 경우
                return True
            x += 1
    if direction == 3: #북쪽
        while (x >= 0):
            if (hallway[x][y] == 'O'): # 장애물이 있는 경우
                return False
            if (hallway[x][y] == 'S'): # 학생이 있는 경우
                return True
            x -= 1
    
    # 학생 미발견
    return False

# 현재 장애물 조합이 있을 때, 학생을 감지할 수 있는지
def check():

    # 모든 선생님의 위치를 하나씩 확인
    for x, y in teachers:

        # 각 선생님이 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            # 학생을 감지할 수 있다면
            if (watch(x, y, i)):
                return True
    # 감지 불가능
    return False

# 빈칸 위치들 중, 3개의 장애물 조합 계산
emptys_total_combi = list(combinations(emptys, 3))

# 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부
find = False

# 장애물 설치 조합에 따라, 선생님이 상, 하, 좌, 우로 학생들을 감시할 수 있는지 확인
for emptys_combi in emptys_total_combi:
    
    # 장애물 설치
    for x, y in emptys_combi:
        hallway[x][y] = 'O'
    
    # 해당 장애물 조합을 통해 학생을 감지할 수 없었다면
    if (check() == False):
        find = True
        break

    # 장애물 제거
    for x, y in emptys_combi:
        hallway[x][y] = 'X'

if (find == True):
    print("YES")
else:
    print("NO")
