import sys

# 모든 학생의 출석 번호
array = [0] * 31

for _ in range(28):

    # 제출자의 출석번호
    n = int(sys.stdin.readline())
    # 제출자는 제출 표시
    array[n] = 1

# 제출하지 않은 학생 별도 저장
result = []
for i in range(1, 31):
    if (array[i] == 0):
        result.append(i)

print(min(result))
print(max(result))



