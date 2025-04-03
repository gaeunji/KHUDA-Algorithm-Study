def solution(words):
    for i in range(len(words)):
        for j in range(len(words)):
           if i != j:
                new_word = words[i] + words[j]
                if new_word == new_word[::-1]:
                    return new_word
    return 0
    

T = int(input())
for i in range(T):
    words = []
    k = int(input())
    for i in range(k):
        word = str(input())
        words.append(word)
    answer = solution(words)
    print(answer)
