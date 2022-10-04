import sys

# A와 B 입력
a, b = map(int, sys.stdin.readline().split())

# 변환 횟수
count = 1

# A보다 B가 클때까지
while (a < b):
    
    # B가 2로 나눠진다면, B를 2로 나누고
    if (b % 2 == 0):
        b = b // 2

    # 나눠지지 않는다면,
    else:
        
        # B의 가장 오른쪽이 1이라면
        if (int(str(b)[-1]) == 1):
            
            # 가장 오른쪽에서 1을 제거한다.
            b = int(str(b)[:-1])
        
        # B의 가장 오른쪽이 1이 아니라면
        else:
            # 변환 불가능
            break

    # 변환 횟수 증가
    count += 1

# A와 B가 같다면
if (a == b):
    print(count)
# 변환 불가능하다면
else:
    print(-1)
