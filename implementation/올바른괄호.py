def solution(p):
    
    # 왼쪽 괄호의 개수
    count = 0
    
    for i in range(len(p)):
        
        # '('라면
        if (p[i] == '('):
            count += 1
        
        # ')'라면
        else:
            
            # 왼쪽 괄호가 없는 상태에서 오른쪽 괄호가 등장했을 경우
            if (count == 0):
                return False
            count -= 1
        
        # 모든 문자를 탐색했는데, 왼쪽 괄호가 닫히지 않았을 경우
        if (i == len(p) - 1 and count >= 1):
            return False
    
    return True