from itertools import permutations

def solution(n, weak, dist):

    # 원본 취약 지점 리스트의 길이
    origin_weak_len = len(weak)
    # 취약 지점 리스트의 길이를 2배 늘려 원형 형태를 일자 형태로 변환
    for i in range(origin_weak_len):
        weak.append(weak[i] + n)

    # 친구 순열 조합 생성
    total_friends = list(permutations(dist, len(dist)))

    # 사용된 친구의 최소 개수
    # 마지막 단계까지 아무 조합으로도 모든 취약 지점 탐색이 불가능했는지 확인하기 위해 +1
    result = len(dist) + 1

    # 변환된 취약 지점 리스트의 탐색 시작 인덱스를 결정
    for start_weak in range(origin_weak_len):

        # 친구 순열 조합을 순서대로 사용
        for friends in total_friends:

            # 투입된 친구의 수
            count = 1
            
            # 투입된 친구가 확인할 수 있는 마지막 위치
            position = weak[start_weak] + friends[count-1]

            # 변환된 취약 지점 리스트의 일정 구간을 탐색
            for search_index in range(start_weak, start_weak + origin_weak_len):

                # 마지막까지 탐색된 위치보다 현재 취약 지점의 값이 크다면
                if (weak[search_index] > position):
                    # 친구 추가
                    count +=1
                    # 친구들을 더 이상 투입할 수 없을 경우
                    if (count > len(dist)):
                        break
                    # 마지막까지 확인된 위치를 업데이트
                    position = weak[search_index] + friends[count-1]
            
            # 투입된 친구의 최소값을 계산
            result = min(result, count)

    # 친구들을 모두 투입해도 탐색하기 어려울 경우
    if (result > len(dist)):
        return -1

    return result       