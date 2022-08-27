def solution(s):

    # 주어진 문자열의 길이로 최소 압축 길이 초기화
    min_len = len(s)

    # 탐색 단위 수를 1부터 문자열 중간 길이까지 늘려가며 확인
    for unit in range(1, (len(s)//2)+1):

        # 결과 문자열
        result = ""    
        
        # 첫 탐색 단위
        previous = s[0:unit]
        
        # 동일한 탐색 단위의 개수
        count = 1
        
        # 탐색 인덱스를 탐색 단위만큼 증가시키며, 이전 탐색 단위와 비교
        for idx in range(unit, len(s), unit):
            
            # 현재 탐색 단위를 슬라이싱
            now = s[idx:idx+unit]

            # 현재 탐색 단위가 이전 탐색 단위와 같다면
            if (now == previous):
                count += 1
            # 현재 탐색 단위가 이전 탐색 단위와 다르다면
            else:
                if (count >= 2):
                    result += str(count) + previous
                else:
                    result += previous
                previous = now
                count = 1

        # 남아있는 문자열에 대해 처리
        if (count >= 2):
            result += str(count) + previous
        else:
            result += previous    

        # 탐색 단위별로 압축 문자열의 길이를 비교해, 최소 압축 문자열의 길이를 저장
        min_len = min(min_len, len(result))

    return min_len
