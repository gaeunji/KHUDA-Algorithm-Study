def solution(numbers):
    
    length = len(numbers)

    answer = []
    for i in range(length):
        for j in range(i,length):
            if i!=j:
                x=numbers[i]+numbers[j]
                answer.append(x)
    answer = set(answer)
    answer = list(answer)
    answer.sort()
    return answer