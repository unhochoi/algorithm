import sys

# 문자열 입력
s = list(sys.stdin.readline().rstrip())

# 0이 연속된 부분
count0 = 0
# 1이 연속된 부분
count1 = 0

# 첫 번째 정수는 곧바로 연속된 부분으로 추가
if (s[0] == '0'):
    count0 += 1
else:
    count1 += 1

# 정수를 순서대로 탐색하며, 연속된 정수가 다른 정수로 바뀔 때, 연속된 부분의 개수 추가
for i in range(len(s)-1): 
    # 연속된 정수가 다음 수에서 다른 정수로 바뀔 때
    if (s[i] != s[i+1]):
        # 다음 수에서 0으로 바뀌는 경우
        if (s[i+1] == '0'):
            count0 += 1
        # 다음 수에서 1로 바뀌는 경우
        else:
            count1 += 1

# 연속된 부분의 개수가 적은 값을 출력
print(min(count0, count1))

