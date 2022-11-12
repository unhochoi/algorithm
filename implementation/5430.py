import sys
from collections import deque

# 테스트 케이스 개수
t = int(sys.stdin.readline())

for _ in range(t):

    # 수행할 함수
    total_command = sys.stdin.readline().rstrip()

    # 배열에 들어있는 수의 개수
    n = int(sys.stdin.readline())

    # 문자열에서 '[', ']'를 제거하고,
    # ',' 기준으로 분리한 뒤, queue에 담기
    q = deque(sys.stdin.readline().rstrip()[1:-1].split(','))

    # 배열이 비어있다면
    if (n == 0):
        # 배열이 비어있어도, R 함수는 문제 없이 실행할 수 있으므로, q를 빈 배열로 초기화
        q = []

    # R 함수의 개수
    r_count = 0

    # 에러 여부
    error = False

    # 순서대로 함수 실행
    for command in total_command:

        # R 함수라면
        if (command == 'R'):

            # R 함수의 개수 추가
            r_count += 1
        
        # D 함수라면
        else:
            
            # 배열에 수가 남아있을 경우
            if (q):
            
                # 현재까지 등장한 R의 개수가 홀수일 경우
                if (r_count % 2 == 1):
                    
                    # reverse 했다고 가정한 뒤, pop 실행
                    q.pop()
                
                # 현재까지 등장한 R의 개수가 홀수일 경우
                else:
                    
                    # 변함 없는 상태라고 가정한 뒤, popleft 실행
                    q.popleft()

            # 배열에 수가 남아있지 않을 경우
            else:
                error = True
                break
    
    # 에러가 발생했다면
    if (error == True):
        print('error')
    
    # 에러가 발생하지 않았다면
    else:
        
        # 모든 함수에 등장한 R의 개수가 홀수라면, 전체 배열 뒤집기
        if (r_count % 2 == 1):
            q.reverse()
            print('[' + ','.join(q) + ']')
        
        # 모든 함수에 등장한 R의 개수가 짝수라면, 그대로 유지
        else:
            print('[' + ','.join(q) + ']')
        
