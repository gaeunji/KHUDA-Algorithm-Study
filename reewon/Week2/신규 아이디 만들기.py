def solution(new_id):
    answer = []
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    for ch in new_id:
        if ch.isdigit() or ch.isalpha() or ch == '-' or ch == '_' or ch == '.':
            answer.append(ch)
    
    # 3단계
    new_id, cnt = [], 0
    for i in range(len(answer)):
        if answer[i] == '.':
            if cnt == 0:
                new_id.append(answer[i])
            cnt += 1
        else:
            cnt = 0
            new_id.append(answer[i])
    
    # 4단계(list가 비어있는지 확인하면서 delete)
    if new_id:
        if new_id[0] == '.':
            del new_id[0]
    if new_id:
        if new_id[-1] == '.':
            del new_id[-1]
    
    # 5단계
    if new_id == []:
        new_id.append('a')
    
    # 6단계
    if len(new_id) > 15:
        del new_id[15:]
        if new_id[-1] == '.':
            del new_id[-1]
    
    # 7단계
    while len(new_id) < 3:
        new_id.append(new_id[-1])
    
    answer = ''.join(new_id)
    return answer
