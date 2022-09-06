
# 현재까지의 결과 구조물을 모두 설치할 수 있는지 확인
def possible(result):

    # 현재까지의 결과 구조물을 다시 확인하기
    for structure in result:

        x, y, a = structure

        # 설치된 구조물이 기둥이라면
        if (a==0):
            
            # 해당 구조물을 설치할 수 있는지 확인 (바닥 위에 있거나, 보의 한쪽 끝 위에 있거나, 다른 기둥의 위일 경우)
            if (y == 0 or [x-1, y, 1] in result or [x, y, 1] in result or [x, y-1, 0] in result):
                continue
            # 설치할 수 없다면
            else:
                return False

        # 설치된 구조물이 보라면
        else:
            
            # 해당 구조물을 설치할 수 있는지 확인 (보의 한쪽 끝 부분이 기둥 위에 있거나, 양쪽 끝부분이 다른 보와 동시에 연결되어 있을 경우)
            if ([x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result)):
                continue
            # 설치할 수 없다면
            else:
                return False
    
    return True

def solution(n, build_frame):
    
    # 결과 구조물
    result = []

    # 명령어 확인하기
    for command in build_frame:

        x, y, a, b = command

        # 설치라면
        if (b == 1):
            # 결과 구조물에 현재 구조물 추가
            result.append([x, y, a])
            # 현재 구조물을 추가할 수 있는지 확인
            if (possible(result)):
                continue    
            # 현재 구조물을 추가할 수 없다면 결과 구조물에서 다시 제거
            else:
                result.remove([x, y, a])
        
        # 삭제라면
        else:
            # 결과 구조물에 현재 구조물 제거
            result.remove([x, y, a])
            # 현재 구조물을 제거할 수 있는지 확인
            if (possible(result)):
                continue
            # 현재 구조물을 제거할 수 없다면 결과 구조물에 다시 추가
            else:
                result.append([x, y, a])

    # 결과 구조물 정렬한 뒤 반환
    return sorted(result)