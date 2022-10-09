import sys

# 입력을 8진수로 변환
n = int(sys.stdin.readline().rstrip(), 8)

# 8진수를 2진수로 변환한 뒤, 맨 앞의 '0b'를 제외한 나머지 출력
print(bin(n)[2:])