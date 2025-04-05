def solution(s):
    answer = []
    idx = 0
    for ch in s:
        if ch == " ":
            answer.append(ch)
            idx = 0
            continue
        if idx%2 == 0:
            answer.append(ch.upper())
        else:
            answer.append(ch.lower())
        idx += 1
    result = "".join(answer)
    return result
