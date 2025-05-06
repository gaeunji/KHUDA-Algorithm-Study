def solution(answers):
    answer = [0, 0, 0]
    ans_len = len(answers)
    
    Stud1 = [1, 2, 3, 4, 5]
    Stud2 = [2, 1, 2, 3, 2, 4, 2, 5]
    Stud3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for idx, ans in enumerate(answers):
        ans = answers[idx]
        if (Stud1[idx%len(Stud1)] == ans) : answer[0] += 1
        if (Stud2[idx%len(Stud2)] == ans) : answer[1] += 1
        if (Stud3[idx%len(Stud3)] == ans) : answer[2] += 1
        
    max_score = max(answer)
    answer = [i+1 for i in range(3) if max_score == answer[i] ]
    
    return answer
