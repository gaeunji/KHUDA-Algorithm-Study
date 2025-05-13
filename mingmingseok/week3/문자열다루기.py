import re

def solution(s):

    answer = re.findall("\d{4,6}",s)
    
    if len(answer)==1 and answer[0] == s and (len(s)==4 or len(s)==6):

        return True
    else :
        return False
