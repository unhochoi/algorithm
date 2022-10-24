def solution(number, k):
    
    # 스택 초기화
    stack = [number[0]]
    
    # 2번째 숫자부터 순서대로 탐색
    for i in range(1, len(number)):
        
        # 스택에 아직 숫자가 남아있다면, 현재 숫자가 스택의 마지막으로 저장된 숫자보다 크다면, 아직 빼기 횟수가 남아있다면
        while (stack and number[i] > stack[-1] and k > 0):
            # 스택의 마지막으로 저장된 숫자 빼기
            stack.pop()
            # 남은 빼기 횟수 감소
            k -= 1

        # 스택에 현재 숫자 삽입하기
        stack.append(number[i])
    
    # k가 남아있는 경우, 스택의 마지막에서 k개를 제거
    if (k != 0):
        stack = stack[:-k]
    
    # 결과 문자열 생성
    return ''.join(stack)