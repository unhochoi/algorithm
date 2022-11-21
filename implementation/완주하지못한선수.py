import collections

def solution(participant, completion):

    # 1. Counter를 사용해, participant의 {참여자의 이름 : 참여자의 수}를 구한다.
    # 2. Counter를 사용해, completion의 {참여자의 이름 : 참여자의 수}를 구한다.
    # 3. 둘의 차를 구하면, 완주하지 못한 선수에 대한 counter가 반환된다.
    answer = collections.Counter(participant) - collections.Counter(completion)
    
    # counter의 key 값을 list화 한 뒤, 첫 번째 요소를 출력한다.
    return list(answer.keys())[0]