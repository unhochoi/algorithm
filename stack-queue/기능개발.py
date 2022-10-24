from collections import deque

def solution(progresses, speeds):
    
    # 결과 리스트
    result = []
    
    # 큐 생성
    q = deque()
    
    # 작업이 끝나기까지 남은 일수 계산
    for i in range(len(progresses)):
        
        # 남은 작업 진도
        remain_task = 100 - progresses[i]
    
        # 작업 진도가 작업 속도와 딱 떨어진다면
        if (remain_task % speeds[i] == 0):
            # 작업이 끝나기까지 남은 일수
            remain_day = remain_task // speeds[i]
        
        # 아니라면
        else:
            # 작업이 끝나기까지 남은 일수
            remain_day = (remain_task // speeds[i]) + 1    
        
        # 작업이 끝나기까지 남은 일수를 큐에 추가
        q.append(remain_day)
    
    # 최댓값
    max_value = -int(1e9)
    
    # 큐가 빌때까지
    while q:
        
        # 큐에서 요소 추출
        now = q.popleft()
        
        # 현재 요소가 이전에 뺏던 요소들 중에 가장 큰 값이라면
        if (max_value < now):
            # 최대값 변경
            max_value = now
            # 새로운 배포 일정을 추가합니다.
            result.append(1)
        
        # 마지막 배포 일정에 기능의 개수를 추가합니다.
        else:
            result[-1] += 1
    
    return result