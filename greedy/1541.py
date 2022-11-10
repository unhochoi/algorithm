import sys

# 입력 문자열
input_ = sys.stdin.readline().rstrip()

# 숫자 배열
num_arr = []

# 입력 문자열을 - 를 기준으로 분리
arr = input_.split('-')

# 각 원소들을 원소들의 합으로 변환
for element in arr:

    # 현재 원소를 + 를 기준으로 분리한 뒤, 원소들의 합으로 변경
    temp = 0
    for num in element.split('+'):
        temp += int(num)

    # 숫자 배열에 삽입
    num_arr.append(temp)

# 숫자 배열에서, 맨 처음의 원소는 더하고 나머지 원소들은 뺍니다.
result = num_arr[0]
for i in range(1, len(num_arr)):
    result -= num_arr[i]

print(result)
