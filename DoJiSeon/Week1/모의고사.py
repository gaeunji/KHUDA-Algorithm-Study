def solution(answers):
    
    stu1 = [1,2,3,4,5]
    stu2 = [2,1,2,3,2,4,2,5]
    stu3 = [3,3,1,1,2,2,4,4,5,5]
    
    s1,s2,s3 = 0 , 0, 0
    score = []
    
    j = 0
    for i in range(len(answers)):
        
        if stu1[i % len(stu1)] == answers[i]:
            s1 += 1
    score.append(s1)
        
    j = 0
    for i in range(len(answers)):
        
        if stu2[i % len(stu2)] == answers[i]:
            s2 += 1
    score.append(s2)
    
    
    for i in range(len(answers)):
        
        if stu3[i % len(stu3)] == answers[i]:
            s3 += 1
    score.append(s3)
    
    maxScore = max(score)
    answer = []
    
    for i in range(len(score)):
        if maxScore == score[i]:
            answer.append(i+1)
    
    
    return answer