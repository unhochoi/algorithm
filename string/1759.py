import sys
from itertools import combinations

# 결과 문자열 길이 l과 알파벳 개수 c
l, c = map(int, sys.stdin.readline().split())

# 모음 전체
temp = ['a', 'e', 'i', 'o', 'u']

# 모음 리스트
a = []
# 자음 리스트
b = []

chars = sys.stdin.readline().split()
for char in chars:
    if (char in temp):
        a.append(char)
    else:
        b.append(char)

# 결과 리스트
result = []

# 모음이 i개일때, 자음은 l-i개 뽑기
for i in range(1, l-1):
    # 모음 조합
    a_combi = list(combinations(a, i))
    # 자음 조합
    b_combi = list(combinations(b, l-i))
    for j in a_combi:
        for k in b_combi:
            result.append(''.join(sorted(j + k)))

result = sorted(result)
for word in result:
    print(word)
