import sys

# 테스트 케이스의 개수
t = int(sys.stdin.readline())

for _ in range(t):

    # 막대의 길이와 개미의 수
    stick_len, ant_count = map(int, sys.stdin.readline().split())

    # 최소 시간 배열
    min_time = []

    # 최대 시간 배열
    max_time = []

    # 개미의 위치
    for _ in range(ant_count):

        # 현재 개미의 위치
        loc = int(sys.stdin.readline())

        # 현재 개미가 땅으로 떨어지는 최소 시간 저장
        min_time.append(min(loc, stick_len - loc))

        # 현재 개미가 땅으로 떨어지는 최대 시간 저장
        max_time.append(max(loc, stick_len - loc))

    # 각 개미가 땅으로 떨어지는 최소 시간 중 제일 큰 값과
    # 각 개미가 땅으로 떨어지는 최대 시간 중 제일 큰 값을 출력
    print(max(min_time), max(max_time))
        

        
