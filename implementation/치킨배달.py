import sys
from itertools import combinations

# 도시의 크기와 치킨집의 최대 개수 입력
n, m = map(int, sys.stdin.readline().split())

# 집 위치
house = []
# 치킨집 위치
chicken = []

# 집과 치킨집의 위치를 저장
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        # 집이라면
        if (row[j] == 1):
            house.append((i, j))
        # 치킨집이라면
        elif (row[j] == 2):
            chicken.append((i, j))

# 전체 치킨집에서 M개를 뽑는 조합 계산
total_chick_combi = list(combinations(chicken, m))

# 치킨집 조합에 따른 도시의 치킨 거리 결과에서, 최소값을 계산하기 위한 변수
result = int(1e9)

# 치킨집 조합에 따른 도시의 치킨 거리 계산
for chick_combi in total_chick_combi:

    # 도시의 치킨 거리를 계산하기 위한 변수
    sum_chick_dist = 0

    # 각 집에서의 치킨 거리를 계산
    for house_location in house:

        # 최소의 치킨 거리를 계산하기 위한 변수
        chick_dist = int(1e9)
        
        for x, y in chick_combi:
            # 각 집에서, 치킨집 별 치킨 거리 비교
            chick_dist = min(chick_dist, abs(house_location[0]-x) + abs(house_location[1]-y))
    
        # 해당 집의 치킨 거리를 도시의 치킨 거리 결과에 덧셈 
        sum_chick_dist += chick_dist

    # 치킨집 조합에 따른 도시의 치킨 거리 결과에서, 최소값을 계산
    result = min(result, sum_chick_dist)

print(result)