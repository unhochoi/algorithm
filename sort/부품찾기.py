import sys

# 부품 개수 및 부품 번호 기록
n = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().rstrip().split()))

# 가게 부품 번호 기록
idx_list = [0]*1000000
for idx in n_list:
    idx_list[idx] = 1

# 손님이 요청한 부품 확인
for idx in m_list:
    if (idx_list[idx] != 1):
        print("no", end=" ")
    else:
        print("yes", end=" ")