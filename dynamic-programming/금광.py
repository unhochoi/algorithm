import sys

# 테스트 케이스 입력
t = int(sys.stdin.readline())

for _ in range(t):
    # 금광 정보 입력
    n, m = map(int, sys.stdin.readline().split())
    gold_input = list(map(int, sys.stdin.readline().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    gold = []
    for i in range(n):
        gold.append(gold_input[i*m:i*m+m])

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위가 없다면
            if ( i == 0 ):
                gold[i][j] += max(gold[i][j-1], gold[i+1][j-1])
            # 왼쪽 아래가 없다면
            elif ( i == n - 1):
                gold[i][j] += max(gold[i-1][j-1], gold[i][j-1])
            # 왼쪽 위와 왼쪽 아래가 다 있다면
            else:
                gold[i][j] += max(gold[i-1][j-1], gold[i][j-1], gold[i+1][j-1])

    # 채굴자가 얻을 수 있는 금의 최대 크기 비교
    result = 0
    for i in range(n):
        result = max(result, gold[i][m - 1])
    
    print(result)