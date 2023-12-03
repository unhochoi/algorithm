import sys

number = list(map(int, sys.stdin.readline().rstrip()))

# dp[i] => i번째 숫자까지 해석할 수 있는 경우의 수
dp = [0] * (len(number)+1)
dp[0] = 1
dp[1] = 1 # 1번째 숫자까지 해석할 수 있는 경우의 수는 1이므로 미리 계산


# 암호가 잘못되어 해석할 수 없는 경우 (첫 번째 숫자가 0일 경우)
if (number[0] == 0):
    print(0)
else:
    for i in range(1, len(number)):

        # dp[0]이 사용되고 있으므로 dp 접근용 idx 재선언
        j = i+1
        
        if (number[i] > 0):     # 마지막 1개의 숫자가 0이면 대응되는 문자가 없음
            dp[j] += dp[j-1]    # 마지막 1개 숫자 이전의 숫자들로 가능했던 경우의 수와 동일하기 때문에, 해당 경우의 수를 더해주기
        
        if (10 <= 10 * number[i-1] + number[i] <= 26): # 마지막 2개의 숫자가 10 이상 26 이하라면
            dp[j] += dp[j-2]    # 마지막 2개 숫자 이전의 숫자들로 가능했던 경우의 수와 동일하기 때문에, 해당 경우의 수를 더해주기

    print(dp[-1]%1000000)