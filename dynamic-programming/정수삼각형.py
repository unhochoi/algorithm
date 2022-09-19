import sys

n = int(sys.stdin.readline())

# 다이나믹 프로그래밍을 위한 DP 테이블 초기화
array = []
for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

# 다이나믹 프로그래밍으로 2번째 줄부터 내려가면서 확인
for i in range(1, n):
    for j in range(i+1):
        # 현재 위치가 가장 왼쪽일 경우
        if (j==0):
            array[i][j] += array[i-1][j]
        # 현재 위치가 가장 오른쪽 일 경우
        elif (j==i):
            array[i][j] += array[i-1][j-1]
        # 나머지 경우
        else:
            array[i][j] += max(array[i-1][j-1], array[i-1][j])

# 마지막 행에서 최대값을 출력
print(max(array[n-1]))
