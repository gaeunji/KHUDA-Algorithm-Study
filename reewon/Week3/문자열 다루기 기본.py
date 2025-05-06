import re

def solution(s):
    if re.fullmatch("\d{4}",s) or re.fullmatch("\d{6}", s):
        return True
    return False
