# 문제
# 수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에 
# 가장 긴 감소하는 부분 수열은 A = {10, 30, 10, 20, 20, 10}  이고, 길이는 3이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 감소하는 부분 수열의 길이를 출력한다.

# 6
# 10 30 10 20 20 10

# 3


import sys

n = int(sys.stdin.readline())
item = list(map(int, sys.stdin.readline().split()))

# 아이템 역순 정렬
item_reversed = item[::-1]
# DP 테이블 생성
# dp = [[0] * n for _ in range(n)]
dp = [1] * n

# print(item_reversed)
for i in range(n):
    pivot = item_reversed[i]
    for j in range(i+1,n):
    #    print(pivot)
    #    print(item_reversed[j])
       if (pivot < item_reversed[j]):
           dp[j] = max(dp[i]+1, dp[j])
    # print(dp)
# print(dp)
print(max(dp))