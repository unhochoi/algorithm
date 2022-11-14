import sys

# 정수 n
n = int(sys.stdin.readline())

# n개의 정수로 이루어진 수열
arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))

# 연속된 부분 숫자들의 합 (첫 번째 요소는 수열의 첫 번째 숫자로 초기화)
sum = [arr[0]]

for i in range(1, n):
    
    # i번째 이전까지 연속된 부분 숫자들의 합보다 i번째 숫자가 큰 경우,
    # 다시 i번째 숫자부터 연속된 부분 숫자들의 합을 구하면 됩니다.
    sum.append(max(sum[i-1] + arr[i], arr[i]))

# 연속된 부분 숫자들의 합 중 최댓값 출력
print(max(sum))
