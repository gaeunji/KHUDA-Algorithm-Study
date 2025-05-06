def solution(s):
    # 단어별로 나누고 단여 길이 받아와서 짝 홀 체인지하기
    str = list(s)
    answer = ''
    count = 0
    for item in str:
        if item != ' ':
            if count % 2 == 0:
                answer += item.upper()
                count += 1
            else:
                answer += item.lower()
                count += 1
        else:
            answer += ' '
            count = 0
			
    return answer