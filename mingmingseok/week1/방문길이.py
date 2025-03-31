def direction(c):
    if c == 'U':
        return [0,1]
    elif c == 'L':
        return [-1,0]
    elif c == 'D':
        return [0,-1]
    elif c == 'R':
        return [1,0]
    else :
        return 0

def solution(dirs):
    #dris는 str 형태
    init_pos = [0,0]
    current_pos = [0,0]
    count = 0
    check_list =[]
    
    for char in dirs:
        c = direction(char)
        new_pos = [current_pos[0] +c[0], current_pos[1]+c[1]]
        if -5<=new_pos[0]<=5 and -5<=new_pos[1]<=5:
            if [current_pos, new_pos] not in check_list and [new_pos, current_pos] not in check_list:
                check_list.append([current_pos, new_pos])  
                count += 1
            current_pos = new_pos
        
    return count