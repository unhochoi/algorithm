import sys

# 테스트 케이스의 개수
t = int(sys.stdin.readline())

for _ in range(t):

    # 정수의 개수
    n = int(sys.stdin.readline())

    # 모든 정수
    array = list(map(int, sys.stdin.readline().split()))

    # 최솟값과 최댓값 출력
    min_value = min(array)
    max_value = max(array)
    print(min_value, max_value)
