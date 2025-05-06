def solution(answers):
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    scores = [0, 0, 0]
    
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):  # patterns 속에 있는 하나가 pattern
            if answer == pattern[i % len(pattern)]: # pattern의 []번째 / j는 수포자 번호
                scores[j] += 1
    # 이 과정이 끝나면 scores에는 [114, 152, 213] 이런 식으로 저장됨.
    answer = []
    for i, score in enumerate(scores):
        if score == max(scores):
            answer.append(i+1)
    return answer