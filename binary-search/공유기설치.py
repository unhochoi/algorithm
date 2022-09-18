import sys

# 집의 개수(N)와 공유기의 개수(C)를 입력 받기
n, c = map(int, sys.stdin.readline().split())

# 전체 집의 좌표 정보를 입력 받기
array = []
for _ in range(n):
    array.append(int(sys.stdin.readline()))
# 이진 탐색 수행을 위해 정렬 수행
array.sort()

# 공유기를 설치할 수 있는 최소 간격
start = 1
# 공유기를 설치할 수 있는 최대 간격
end = array[-1] - array[0]
# 최종 공유기 설치 간격
result = 0

def bs(array, start, end):

    global result

    if (start > end):
        return result

    # 가장 처음으로 공유기를 설치하는 집의 위치
    recent_dist = array[0]
    # 공유기 설치 개수
    count = 1
    # 공유기 설치 간격
    mid = (start + end) // 2
    
    # 현재의 mid 값을 이용해 공유기를 설치
    for i in range(1, n):
        # 가장 최근에 공유기를 설치한 집과 mid 간격 이상으로 떨어졌다면, 공유기 설치
        if (array[i] - recent_dist >= mid):
            recent_dist = array[i]
            count += 1
    
    # 설치된 공유기의 개수가 c개 이상이라면, 해당 간격을 저장하고, 간격을 더 늘리기
    if (count >= c):
        result = mid # 최적의 결과를 저장
        return bs(array, mid+1, end)

    # 설치된 공유기의 개수가 c개 미만이라면, 간격을 더 줄이기
    else:
        return bs(array, start, mid-1)

print(bs(array, start, end))