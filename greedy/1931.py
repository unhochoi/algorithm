import sys

# 회의의 수
n = int(sys.stdin.readline())

# 회의 시간
meeting_times = []

# 회의의 시작 시간과 끝나는 시간
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meeting_times.append((start, end))

# 회의 시간을 종료 시간 기준 및 시작 시간 기준으로 정렬
meeting_times = sorted(meeting_times, key = lambda x : (x[1], x[0]))

# 최대 회의 개수
count = 1
# 이전 회의 종료 시간
end_time = meeting_times[0][1]

for i in range(1, n):
    # 다음 회의 시작 시간이 이전 회의 종료 시간보다 크거나 같다면
    if (meeting_times[i][0] >= end_time):
        # 이전 회의 종료 시간 업데이트
        end_time = meeting_times[i][1]
        # 최대 회의 개수 증가
        count += 1

print(count)