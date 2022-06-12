import sys

# 정수 X를 입력받기
x = int(sys.stdin.readline().rstrip())

# DP 테이블 생성
dp_table = [0] * 30001

# 바텀업 진행
for i in range(2, x+1):

    # 현재 값에서 -1 을 했을 때가 최소 연산 횟수라고 가정하고, 
    # 해당 값에서 +1 함으로써, 현재 값까지의 최소 연산 횟수를 default로 지정
    dp_table[i] = dp_table[i-1] + 1
    # 현재 값을 5로 나눴을 때의 연산 횟수와 현재 값을 -1로 뺐을 때의 연산 횟수 중, 최솟값을 최소 연산 횟수로 지정
    if (dp_table[i] % 5 == 0):
        dp_table[i] = min(dp_table[i], dp_table[i // 5] + 1)
    # 현재 값을 3으로 나눴을 때의 연산 횟수와 현재 값을 -1로 뺐을 때의 연산 횟수 중, 최솟값을 최소 연산 횟수로 지정
    if (dp_table[i] % 3 == 0):
        dp_table[i] = min(dp_table[i], dp_table[i // 3] + 1)
    # 현재 값을 2로 나눴을 때의 연산 횟수와 현재 값을 -1로 뺐을 때의 연산 횟수 중, 최솟값을 최소 연산 횟수로 지정
    if (dp_table[i] % 2 == 0):
        dp_table[i] = min(dp_table[i], dp_table[i // 2] + 1)

print(dp_table[x])
