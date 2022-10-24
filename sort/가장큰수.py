def solution(numbers):
    
    # 각 숫자들을 문자열로 변환
    numbers = list(map(str, numbers))
    
    # 각 문자열을 3번 반복한 문자열로 변환한 뒤, 내림차순 정렬
    numbers.sort(key = lambda x:x*3, reverse=True)
    
    # 각 문자열들을 하나의 문자열로 통합
    # 모든 문자열이 0일 때(‘000’)를 처리하기 위해, 문자열을 int로 변환한 뒤 다시 str로 변환
    return str(int(''.join(numbers)))