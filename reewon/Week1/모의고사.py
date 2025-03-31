def solution(answers):
    answer = []
    pattern = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    correct = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == pattern[0][i%5]:
            correct[0] += 1
        if answers[i] == pattern[1][i%8]:
            correct[1] += 1
        if answers[i] == pattern[2][i%10]:
            correct[2] += 1
    
    # 문제를 최대로 많이 맞춘 사람 찾기
    max = 0
    for i in range(3):
        if correct[i] > max:
            max = correct[i]
            if len(answer) != 0:
                del answer[0]
            answer.append(i+1)
        # max가 같은 경우를 위한 코드
        elif correct[i] == max:
            answer.append(i+1)
    return answer
