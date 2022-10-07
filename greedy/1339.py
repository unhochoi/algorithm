import sys

# 알파벳의 자릿수 저장
dic = {}

# 단어의 개수
n = int(sys.stdin.readline())

# 알파벳에 따른 알파벳의 자릿수 저장
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    for i in range(len(word)):
        # 해당 알파벳의 자릿수가 이미 있다면
        if (word[i] in dic):
            dic[word[i]] += 10**(len(word)-i-1)
        # 해당 알파벳의 자릿수가 없다면
        else:
            dic[word[i]] = 10**(len(word)-i-1)

# 사전의 모든 값들을 결과 리스트에 추가
result = []
for value in dic.values():
    result.append(value)

# 결과 리스트 내림차순 정렬
result.sort(reverse=True)

sum = 0
num = 9
for value in result:
    sum += value * num
    num -= 1

print(sum)

