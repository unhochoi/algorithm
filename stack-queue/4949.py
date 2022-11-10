import sys

while True:
    
    line = sys.stdin.readline().rstrip()

    if line == '.':
        break

    # 스택 생성
    stack = []

    # {닫는괄호 : 여는괄호} 형식으로 사전 생성
    dict = {')' : '(', ']' : '['}

    # 결과
    result = "yes"

    # 문자 검색
    for char in line:
        
        # 열린 괄호라면
        if char in '([':
            # 스택에 추가
            stack.append(char)
        
        # 닫힌 괄호라면
        if char in ')]':
            
            # 스택에 열린 괄호가 없다면
            if (len(stack) == 0):
                result = "no"
                break
            
            else:
                # 스택의 TOP과 짝이 맞지 않는다면
                if (dict[char] != stack.pop()):
                    result = "no"
                    break
    
    # 스택에 열린 괄호가 남아있다면
    if (len(stack) > 0):
        print("no")
    else:
        print(result)
            