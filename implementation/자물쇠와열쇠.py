# 2차원 리스트 90도 회전하기
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 회전된 결과 리스트
    # 모든 요소값을 90도 회전
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 자물쇠의 홈부분이 모두 1로 채워졌는지 확인
def check(new_lock):
    for i in range(len(new_lock)//3, (len(new_lock)//3)*2):
        for j in range(len(new_lock)//3, (len(new_lock)//3)*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    # 자물쇠의 크기 측정
    n = len(lock)
    # 열쇠의 크기 측정
    m = len(key)
    # 자물쇠의 크기 확장
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    
    # 열쇠를 회전한 뒤, 해당 열쇠로 자물쇠를 탐색하며, 이를 반복함
    for _ in range(4):
        # 열쇠 회전
        key = rotate_a_matrix_by_90_degree(key)
        
        for i in range(n*2):
            for j in range(n*2):
                # 자물쇠에 열쇠 채우기
                for k in range(m):
                    for l in range(m):
                        new_lock[i+k][j+l] += key[k][l]
                
                # 자물쇠의 홈부분이 모두 1로 채워졌는지 확인
                if (check(new_lock) == True):
                    return True
                
                # 자물쇠에서 열쇠 다시 빼기
                for k in range(m):
                    for l in range(m):
                        new_lock[i+k][j+l] -= key[k][l]
    
    return False