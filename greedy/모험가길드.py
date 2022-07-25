import sys

# 모험가 수
n = int(sys.stdin.readline().rstrip())
# 공포도 배열
data = list(map(int, sys.stdin.readline().rstrip().split()))
# 공포도 배열 정렬
data.sort()

# 총 그룹의 수
result = 0
# 현재 그룹의 인원 수
count = 0

# 공포도 배열 탐색
for horror in data:
    # 현재 그룹에 인원 추가
    count += 1
    # 현재 그룹의 인원이 탐색한 공포도보다 크거나 같으면, 바로 그룹 결성
    if (count >= horror):
        result += 1
        count = 0 # 새로운 그룹을 결성해야하므로, 현재 그룹에 포함된 인원 수는 초기화

# 총 그룹의 수 출력
print(result)
    
