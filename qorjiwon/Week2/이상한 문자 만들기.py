def solution(s):
    words = s.split(' ')
    return ' '.join(''.join([e.lower() if idx%2 else e.upper() for idx, e in enumerate(str)]) for str in words)

# split 사용할 때 조심
# '  ab  '.split()
# 결과 : ['', '', 'ab', '', '']
