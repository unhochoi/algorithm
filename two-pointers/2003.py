import sys

n, m = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))

# 구간 초기화
start, end = 0, 1

# m이 되는 경우의 수
count = 0

while (start <= end and end <= n):

    # 구간의 합 계산
    total = sum(arr[start:end])

    # 구간의 합이 목푯값보다 작다면
    if (total < m):
        # 끝 idx를 오른쪽으로 한 칸 이동
        end += 1

    # 구간의 합이 목푯값보다 크다면
    elif (total > m):
        # 시작 idx를 오른쪽으로 한 칸 이동
        start += 1

    # 구간의 합이 목푯값과 같다면
    else:
        # 경우의 수 증가
        count += 1
        # 끝 idx를 오른쪽으로 한 칸 이동
        end += 1

print(count)