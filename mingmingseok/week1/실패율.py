def solution(N, stages):
    #N : 전체 스테이지의 개수
    #stages : 게임을 이용하는 사용자가 현재 멈춰있는 스테이지 번호

    stage_fails = [0 for _ in range (N)]
    for i in range(N):
        stage_fails[i] = stages.count(i+1)
        
    stage_length = len(stages)
    fail_rates = []
    
    for i in range(N):
        if stage_length ==0 :
            fail_rate = 0
        else :
            fail_rate = stage_fails[i]/stage_length
        fail_rates.append((i+1,fail_rate))
        stage_length = stage_length - stage_fails[i]
    
    fail_rates.sort(key=lambda x: (-x[1],x[0]))
    print(fail_rates)
    answer = [x[0] for x in fail_rates]
    return answer