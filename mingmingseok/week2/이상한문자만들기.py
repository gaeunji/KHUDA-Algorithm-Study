def solution(s):
    count = 0
    answer = ''
    for c in s:
        if c == ' ' : 
            answer += ' '
            count =0
            
        else :
            if count %2 == 0 : 
                s = c.upper()
                answer+=s
                count +=1
            else : 
                s = c.lower()
                answer +=s
                count +=1
    
    return answer