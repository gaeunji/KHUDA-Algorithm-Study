import copy

def solution(N, stages):
    
    # N 개의 스테이지 , stages = 사람 수 , 마지막까지 다 깬사람은 n+1
    # 실패율 계산은 그 스테이지 사람 수 / 전체 사람 비율
    # 앞에서부터 클리어 못한 사람 수를 전체 인원 수에서 쳐내야함.
    
    people = len(stages) # 사람 수
    fail = []
    
    for i in range(1, N+1):
        check = 0
        for j in range(len(stages)):
                if i == stages[j]:
                    check += 1
        failure = check/people
        fail.append(failure)
        
        people -= check
    
    origin = copy.deepcopy(fail)

    fail.sort(reverse=True)

    print(fail)
    print(origin)
    answer = []
    for i in range(N):
        for j in range(N):
            if fail[i] == origin[j] and answer.count(j+1) == 0:
                answer.append(j+1)
                break
            
            
    return answer
