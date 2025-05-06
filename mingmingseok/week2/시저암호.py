def solution(s, n):
    answer = ''

    print(ord('a'))
    print(ord('z'))
    print(ord('A'))
    print(ord('Z'))
    
    for c in s:
        if c ==' ':
            answer += ' '
        else: 
            new_order = ord(c) + n
            if new_order > ord('z'):
                new_order = new_order - 26
            
            elif ord('Z') < new_order and ord(c) <= ord('Z') :
                new_order = new_order - 26
            answer += chr(new_order)
            
        
    return answer