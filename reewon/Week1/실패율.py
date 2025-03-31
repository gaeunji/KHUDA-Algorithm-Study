def solution(N, stages):
    answer = []
    failRate = [0]*N
    for i in range(1, N+1):
        # 현재 스테이지에 머문 사용자 수
        staying = 0
        # 스테이지를 성공하거나 머물고 있는 사용자 수
        total = 0
        for x in stages:
            if x > i:
                total += 1
            elif x == i:
                staying += 1
                total += 1
        if total == 0:
            failRate[i-1] = 0
        else:
            failRate[i-1] = staying / total
    
    # (스테이지 번호, 실패율) 형태의 튜플로 이루어진 리스트
    new_failRate = list(enumerate(failRate))
    # 실패율을 내림차순으로, 같은 값에서는 오름차순으로 정렬
    new_failRate.sort(key=lambda x: (-x[1], x[0]))
    for x in range(len(new_failRate)):
        answer.append(new_failRate[x][0]+1)
            
    return answer
