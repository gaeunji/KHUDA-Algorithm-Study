def check3(s):
    answer = ''
    prev_c = ''
    for c in s:
        if c =='.' and prev_c =='.':
            continue
        else :
            answer+=c
            prev_c = c
    return answer

def check4(s):
    answer = ''
    length = len(s)
    for c in range(length):
        if s[c] =='.' and (c == 0 or c == length-1):
            continue
        else :
            answer+= s[c]
            
    return answer

def check5(s):
    if s == '':
        s = "a"
    return s

def check6(s):
    if len(s)>=16:
        s = s[:15]
        if s[14] == '.':
            s = s[:14]
    return s

def check7(s):
    if len(s)<=2:
        while (len(s)<3):
            s += s[-1]
    return s

def solution(new_id):
    answer = ''
    #step1
    new_id = new_id.lower()

    #step2
    for c in new_id:
        if c in ['-','_','.'] or ord('0')<=ord(c)<=ord('9') or ord('a')<=ord(c)<=ord('z'):
            answer+=c
    #step3
    answer = check3(answer)
    
    #step4
    answer = check4(answer)
    
    #step5
    answer = check5(answer)
    
    #step6
    answer = check6(answer)
    
    #step7
    answer = check7(answer)
    
    return answer