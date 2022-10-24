def solution(s):

    # {닫는괄호 : 여는괄호} 형식으로 사전 생성
    dic = {')' : '(', ']' : '[', '}': '{'}

    # 스택 생성
    stack = []

    # 문자 검색
    for char in s:

        # 문자가 여는 괄호라면
        if (char in '({['):
            # 스택에 삽입
            stack.append(char)

        # 문자가 닫는 괄호라면
        else:
            
            # 스택에 열린 괄호가 남아있다면
            if (stack):
                
                # 스택 top의 열린 괄호
                top = stack.pop()

                # 해당 닫힌 괄호와 스택 top의 열린 괄호가 짝이 맞지 않는다면
                if (dic[char] != top):
                    return False
            
            # 스택이 비어있다면
            else:
                return False

    return True
    

print(solution("{{}}"))
print(solution("({})[]"))
print(solution("[)"))
print(solution("]()["))
print(solution("([())]"))
