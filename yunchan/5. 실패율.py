def solution(N, stages):
    answer = []
    total_players = len(stages)

    for stage in range(1, N + 1):
        # 현재 스테이지에 머무르고 있는 사용자 수 구하기
        failed = 0
        for s in stages:
            if s == stage:
                failed += 1

        # 실패율 계산
        if total_players == 0:
            failure_rate = 0
        else:
            failure_rate = failed / total_players

        answer.append([stage, failure_rate])

        # 다음 스테이지로 갈 사람 수 갱신
        total_players -= failed

    # 실패율 기준 내림차순, 같으면 스테이지 번호 오름차순 정렬
    for i in range(len(answer)):
        for j in range(i + 1, len(answer)):
            if answer[i][1] < answer[j][1] or (answer[i][1] == answer[j][1] and answer[i][0] > answer[j][0]):
                temp = answer[i]
                answer[i] = answer[j]
                answer[j] = temp

    # 스테이지 번호만 남기기
    for i in range(len(answer)):
        answer[i] = answer[i][0]

    return answer
