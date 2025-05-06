def solution(s):
    answer = []
    flag = True
    for i in range(len(s)):
        if  s[i] == ' ': 
            answer.append(s[i].upper())
            flag = True
        
        else:
            if flag:
                answer.append(s[i].upper())
            else:
                answer.append(s[i].lower())
            flag = not flag

    res = "".join(answer)
    return res
