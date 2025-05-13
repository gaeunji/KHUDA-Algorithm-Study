def solution(answers):
    answer = []
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score1 = 0
    score2 = 0
    score3 = 0
    
    # 각 수포자별로 답을 맞춘 개수 세기
    for i in range(len(answers)):
        if answers[i] == person1[i % len(person1)]:
            score1 += 1
        if answers[i] == person2[i % len(person2)]:
            score2 += 1
        if answers[i] == person3[i % len(person3)]:
            score3 += 1
    
    # 가장 많은 점수를 맞힌 사람의 점수를 찾기
    max_score = max(score1, score2, score3)
    
    # 가장 많이 맞힌 사람을 리스트로 반환
    if score1 == max_score:
        answer.append(1)
    if score2 == max_score:
        answer.append(2)
    if score3 == max_score:
        answer.append(3)
    
    return answer
