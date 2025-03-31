def solution(N, stages):
    answer = [0]
    
    # 0, 1, ..., N+1 푸하하하 
    stages_count = [0] * (N+2)
    
    # 0, 1, ..., stage의 길이 
    for i in range(len(stages)):
        stages_count[stages[i]] += 1
    # [0, 1, 3, 2, 1, 0, 1]
    
    prev = len(stages)
    for i in range(1, N+1):
        if prev > 0:
            answer.append(stages_count[i] / prev)
            prev -= stages_count[i]
        else:
            answer.append(0)
    
    sorted_indexes = sorted(range(1, N+1), key=lambda i: answer[i], reverse=True)
    
    return sorted_indexes

# [2, 1, 2, 6, 2, 4, 3, 3]
