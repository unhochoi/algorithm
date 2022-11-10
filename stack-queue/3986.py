import sys

# 단어의 수
n = int(sys.stdin.readline())

# 좋은 단어의 수
result = 0

for i in range(n):
    
    line = sys.stdin.readline().rstrip()

    # 첫 번째 문자는 스택에 바로 삽입
    stack = [line[0]]

    for j in range(1, len(line)):

        # 스택에 문자가 없다면, 해당 문자는 바로 삽입
        if (len(stack) == 0):
            stack.append(line[j])
        
        # 스택에 문자가 있다면
        else:
            # 스택의 TOP에 위치한 문자
            top = stack[-1]

            # 현재 탐색 중인 문자가 Stack의 TOP과 동일하다면, Stack의 TOP을 제거
            if line[j] == top:
                stack.pop()
            
            # Stack의 TOP과 동일하지 않다면, 현재 문자를 Stack에 삽입
            else:
                stack.append(line[j])

    # 스택에 문자가 남아있지 않다면
    if (len(stack) == 0):
        result += 1

print(result)