import sys

# 식량창고의 개수와 식량창고에 저장된 식량 개수 입력 받기
n = int(sys.stdin.readline().rstrip())
n_list = list(map(int,sys.stdin.readline().rstrip().split()))

# DP 테이블 생성, idx 번쨰 식량 창고까지 얻을 수 있는 최대 식량값 저장
dp_table = [0] * 100

# 바텀업 탐색
dp_table[0] = n_list[0]
dp_table[1] = max(n_list[0], n_list[1])
for i in range(2, n):
    dp_table[i] = max(n_list[i-1], n_list[i-2] + n_list[i])

print(dp_table[n-1])