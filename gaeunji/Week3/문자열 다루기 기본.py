import re

def solution(s):
    answer = True
    
    answer = bool(re.fullmatch(r"\d{4}|\d{6}", s))
    
    
    return answer
