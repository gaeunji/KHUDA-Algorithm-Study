def solution(s, n):
    arr = []
    answer = ''
    for i in range(len(s)):
        if s[i].islower(): # 소문자
            low = ord(s[i])
            if low+n > 122:
                low = ord('a') + (n - (ord('z')-low) -1)
            else:
                low += n
            arr.append(chr(low))
        elif s[i].isupper(): # 대문자
            up = ord(s[i])
            if up+n > 90:
                up = ord('A') + (n - (ord('Z') - up) -1)
            else:
                up += n
            arr.append(chr(up))
        else:
            arr.append(s[i])
            
    answer = "".join(arr)
    print(answer)
    
    return answer