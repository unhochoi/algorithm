import sys
import math

# m과 n 입력
m, n = map(int, sys.stdin.readline().split())

# 소수 판별 결과를 저장하기 위한 리스트 초기화
# 처음에는 모든 수가 소수인 것으로 초기화
array = [True] * (1000001)

# 1은 소수가 아님
array[1] = False

# 2부터 n의 제곱근까지 에라토스테네스의 체 진행
for i in range(2, int(math.sqrt(n))+1):
    # i가 아직 남아있는 소수인 경우
    if array[i] == True:
        # i를 제외한 i의 모든 배수를 제거하기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# m 이상 n 이하의 소수를 모두 출력
for i in range(m, n+1):
    if (array[i] == True):
        print(i)
