import sys

# 입력 문자열
s = list(map(int, list(sys.stdin.readline().rstrip())))

# 첫 번째 정수를 초기 결과값으로 지정
result = s[0]

# 두 번째 정수부터 탐색 시작
for i in range(1, len(s)):
    # 해당 정수가 1 이하이거나, 초기 결과값이 1 이하일 경우
    if (s[i] <= 1 or result <= 1):
        # 결과값에 해당 수를 더한다.
        result += s[i]
    # 해당 정수가 2 이상일 경우
    else:
        # 현재 결과값에 해당 수를 곱한다.
        result *= s[i]

print(result)