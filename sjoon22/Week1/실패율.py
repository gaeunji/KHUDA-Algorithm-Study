def solution(N, stages):
    challenge = [0] * (N+2)
    clear = [0] * (N+2)
    fails = [0.] * (N)
    
    # 각 스테이지 도달 인원 세기
    for stage in stages:
        for i in range(len(challenge)):
            if i <= stage:
                challenge[i] += 1

    # 각 스테이지 클리어 인원 세기
    for stage in stages:
        for i in range(len(clear)):
            if i <= (stage - 1):
                clear[i] += 1

    # 실패율 계산
    for i in range(len(fails)):
        if challenge[i+1] == 0:
            fails[i] = 0
        else:
            fails[i] = (challenge[i+1] - clear[i+1]) / challenge[i+1]

    # 인덱스와 함께 정렬
    indexed_fails = [(i + 1, fail) for i, fail in enumerate(fails)]
    indexed_fails.sort(key=lambda x: x[1], reverse=True)

    # 정렬된 스테이지 번호만 추출
    answer = [stage for stage, fail in indexed_fails]
    return answer

# complexity 높아서 틀림 ... 속상하다 .. 내 최선이였는데 .. test 결과 3문제만 시간 초과 ..
# 나중에 다시 풀기 ... ㅎㅎ