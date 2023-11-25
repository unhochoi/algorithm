import sys

N, K = map(int, sys.stdin.readline().split())
num = list(sys.stdin.readline())
k = K # 기존 K 값 저장
stack = []

for i in range(len(num)):
    # 뺄 수 있는 횟수가 남아있고, 스택의 값이 남아있고, 현재 값이 stack의 최근값보다 클 경우 POP
    while (k > 0 and stack and num[i] > stack[-1]):
        stack.pop()
        k -= 1
    # 그 외 경우엔 현재 값을 stack에 삽입
    stack.append(num[i])

# 예외 케이스) 5 2 / 19876 일 경우, 답은 987
print("".join(stack[:N-K]))