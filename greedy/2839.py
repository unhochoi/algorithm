import sys

# 설탕 무게
n = int(sys.stdin.readline())
# 봉지 개수
bag = 0

while n >= 0 :
    if n % 5 == 0 :         # 남은 설탕이 5로 나눠떨어진다면
        bag += (n // 5)     # 5로 나눈 몫을 봉지 개수에 추가
        print(bag)
        break
    
    n -= 3      # 남은 설탕이 5로 나눠떨어지지않는다면, 3씩 덜어내기
    bag += 1    # 봉지 개수 추가

else:
    print(-1)