import sys

# 양수 n을 문자열 형식으로 입력 받음
n = sys.stdin.readline().rstrip()

# 0이 존재하는지
zero = False
# 각 자릿수의 합
sum = 0

for num in n:
    
    # 0이 존재한다면
    if (int(num) == 0):
        zero = True
    # 각 자릿수를 더하기
    sum += int(num)

# 0이 존재하지 않는다면
if (zero == False):
    print(-1)
# 각 자릿수의 합이 3으로 나누어떨어지지 않는다면
elif (sum % 3 != 0):
    print(-1)
# 문제 없는 경우
else:
    # 각 자릿수를 내림차순 정렬한 뒤, 문자열로 변환
    print(''.join(sorted(n, reverse = True)))

