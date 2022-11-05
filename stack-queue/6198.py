import sys

# 빌딩의 개수
n = int(sys.stdin.readline())

# 빌딩들의 높이
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

# 각 빌딩들이 바라볼 수 있는 빌딩의 개수
result = 0

# Stack 초기화 (빌딩의 높이)
stack = []

# 모든 빌딩 탐색
for i in range(n):

    # Stack에 빌딩의 정보가 존재한다면
    while stack:
        
        # 현재 탐색하고 있는 빌딩의 높이가 Stack TOP보다 크거나 같다면
        if (arr[i] >= stack[-1]):
            # 현재 탐색하고 있는 빌딩의 높이가 TOP보다 작아질때까지 Stack TOP 제거
            stack.pop()

        # 현재 탐색하고 있는 빌딩의 높이가 Stack TOP보다 작다면
        else:
            # Stack에 존재하는 빌딩 수 만큼 결과에 덧셈
            result += len(stack)
            break

    # 현재 탐색하고 있는 빌딩의 정보를 Stack에 삽입 (빌딩의 높이)
    stack.append(arr[i])

# 결과 출력
print(result)
