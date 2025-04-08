def solution(s, n):
    s = list(s)
    for idx, ch in enumerate(s):
        if ch.islower():
            s[idx] = chr(ord('a')+(ord(ch)+n-ord('a'))%26)
        elif ch.isupper():
            s[idx] = chr(ord('A')+(ord(ch)+n-ord('A'))%26)
            
    return  ''.join(s)
