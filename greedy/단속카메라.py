def solution(routes):
    
    # 진출 시간을 기준으로 오름차순 정렬
    routes.sort(key = lambda x:x[1])

    # 카메라 설치 위치 초기화
    camera = -int(1e9)
    
    # 카메라 설치 개수
    count = 0
    
    # 차량의 이동 경로 탐색
    for route in routes:
        # 현재 설치된 카메라의 위치보다 다음 차량의 진입 지점이 클 경우, 
        if (camera < route[0]):
            # 카메라를 새롭게 설치
            camera = route[1]
            count += 1
    
    return count
    
    
    