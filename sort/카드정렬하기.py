import sys
import heapq

# 숫자 카드 묶음 개수 입력
n = int(sys.stdin.readline())

# 우선순위 큐에 숫자 카드 묶음 입력
cards = []
for _ in range(n):
    heapq.heappush(cards, int(sys.stdin.readline()))

result = 0

# 우선순위 큐의 숫자 카드 묶음이 2개 이상일때까지 진행
while len(cards) != 1:

    # 가장 작은 2개의 카드 묶음 꺼내기
    first = heapq.heappop(cards)
    second = heapq.heappop(cards)

    # 카드 묶음을 합쳐서 다시 삽입
    result += first + second
    heapq.heappush(cards, first + second)

print(result)