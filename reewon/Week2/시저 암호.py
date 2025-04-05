def solution(s, n):
    answer = []
    for ch in s:
        if ch == " ":
            answer.append(ch)
            continue
        if ch.islower():
            if ord(ch) + n > ord('z'):
                answer.append(chr(ord('a')+(n-(ord('z')-ord(ch))-1)))
            else:
                answer.append(chr(ord(ch)+n))
        elif ch.isupper():
            if ord(ch) + n > ord('Z'):
                answer.append(chr(ord('A')+(n-(ord('Z')-ord(ch))-1)))
            else:
                answer.append(chr(ord(ch)+n))
    result = "".join(answer)
    return result
