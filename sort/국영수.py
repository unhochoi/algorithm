import sys

# 학생 수 입력
n = int(sys.stdin.readline())

# 결과 배열
result = []

# 이름과 국영수 성적 입력
for _ in range(n):
    name, k, e, m = sys.stdin.readline().split()
    result.append((name, int(k), int(e), int(m)))

result = sorted(result, key = lambda x: (-x[1], x[2], -x[3], x[0]))

# 정렬된 학생 정보에서 이름만 출력
for element in result:
    print(element[0])

