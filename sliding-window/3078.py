import sys
from collections import defaultdict

n, k = map(int, sys.stdin.readline().split())

# 성적순으로 나열된 학생의 이름 길이를 저장
arr = []
for _ in range(n):
    arr.append(len(sys.stdin.readline().rstrip()))

# 윈도우 내 학생들에 대한 {이름 길이 : 인원} 저장
dict = defaultdict(int)

# 친구 쌍의 수
count = 0

for end in range(n):

    # 윈도우를 오른쪽으로 한 칸 씩 이동
    if (end > k):
        # 구간에서 빠지는 학생에 대한 이름 길이 인원을 감소
        dict[arr[end-k-1]] -= 1

    # 구간에 추가되는 학생의 이름 길이와 동일한 이름 길이를 가진 학생이 있다면, 친구 쌍의 수 증가
    count += dict[arr[end]]
    
    # 구간에 추가되는 학생에 대한 이름 길이 인원을 추가
    dict[arr[end]] += 1

print(count)