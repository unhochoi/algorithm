import sys

n = sys.stdin.readline().rstrip()

# 왼쪽 부분과 오른쪽 부분의 자릿수 합 계산
leftsum = sum(list(map(int, n[0:len(n)//2])))
rightsum = sum(list(map(int, n[len(n)//2:])))

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if (leftsum == rightsum):
    print("LUCKY")
else:
    print("READY")