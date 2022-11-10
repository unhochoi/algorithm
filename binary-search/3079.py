# import sys

# # 심사대의 개수와 심사를 받는 인원
# n, m = map(int, sys.stdin.readline().split())

# # 각 심사대의 심사 시간
# arr = []
# for _ in range(n):
#     arr.append(int(sys.stdin.readline()))

# # m명을 심사할 수 있는 최소 시간을 찾기 위해 
# # [0 ~ m명을 모두 심사했을 때 가능한 최대 시간]을 start, end 범위로 설정
# start, end = min(arr), max(arr) * m

# # m명을 심사할 수 있는 최소 시간 초기화
# result = max(arr) * m

# while (start <= end):

#     # m명을 심사할 수 있는 최소 시간을 찾기 위해, start와 end의 중간 시간을 mid로 설정
#     mid = (start + end) // 2

#     # mid 시간 동안 심사를 진행한다고 할 때
#     # 각각의 심사대에서 심사할 수 있는 최대 인원 수를 파악한 뒤, 전체 인원을 파악
#     total = 0
#     for i in range(n):
#         total += mid // arr[i]

#     # mid 시간 동안 심사할 수 있는 전체 인원 수가 m명 이상이라면
#     if (total >= m):
#         # 심사 시간을 더 줄이기
#         end = mid - 1
#         # 현재까지의 최소 시간을 저장
#         result = min(result, mid)

#     # mid 시간 동안 심사할 수 있는 전체 인원 수가 m명 이하라면    
#     else:
#         # 심사 시간을 더 늘리기
#         start = mid + 1

# print(result)

print(int(1e9))