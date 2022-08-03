import sys

n = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().rstrip().split()))

# 동전 오름차순 정렬
coins.sort()

# 목푯값 설정
target = 1
# 동전 탐색
for coin in coins:
    # 현재 동전이 못푯값보다 크다면, 해당 목푯값은 만들 수 없음
    if (coin > target):        
        break
    # 목푯값 갱신
    target += coin

# 만들 수 없는 목푯값 출력
print(target)
