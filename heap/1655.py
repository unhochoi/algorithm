import sys
import heapq

n = int(sys.stdin.readline())

leftheap = []
rightheap = []

for _ in range(n):

    # 현재 숫자
    num = int(sys.stdin.readline())

    # leftheap의 길이가 rightheap의 길이와 같다면
    if (len(leftheap) == len(rightheap)):
        # leftheap에 현재 숫자를 음수 형태로 삽입
        heapq.heappush(leftheap, -num)
    
    # leftheap의 길이가 rightheap의 길이와 다르다면
    else:
        # rightheap에 현재 숫자를 삽입
        heapq.heappush(rightheap, num)

    # 양쪽 heap에 요소들이 존재한다면,
    # leftheap의 루트에 음수를 곱한 값이 rightheap의 루트보다 크다면
    if (len(leftheap) >= 1 and len(rightheap) >= 1 and -leftheap[0] > rightheap[0]):
        
        # leftheap의 루트를 제거하고, 
        leftroot = heapq.heappop(leftheap)
        # leftheap의 루트에 음수를 곱한 값을 rightheap에 삽입
        heapq.heappush(rightheap, -leftroot)

        # rightheap의 루트를 제거하고, 
        rightroot = heapq.heappop(rightheap)
        # rightheap의 루트에 음수를 곱한 값을 leftheap에 삽입
        heapq.heappush(leftheap, -rightroot)

    # leftheap의 루트에 음수를 곱한 뒤 출력
    print(-leftheap[0])






