def solution(dirs):
    answer = 0
    # 좌표평면을 행렬로 표현((-5,-5)를 coordinate[0][0]으로)
    # U, D, R, L 순
    # False는 해당 길이 쓰이지 않음을 표현
    coordinate = [[[False, False, False, False] for _ in range(11)] for _ in range(11)]
    i, j = 5, 5
    
    for x in dirs:
        if x == "U":
            if j+1 < len(coordinate):
                if coordinate[i][j][0] == True:
                    j += 1
                else:
                    coordinate[i][j][0] = True
                    j += 1
                    coordinate[i][j][1] = True
                    answer += 1
        elif x == "R":
            if i+1 < len(coordinate):
                if coordinate[i][j][2] == True:
                    i += 1
                else:
                    coordinate[i][j][2] = True
                    i += 1
                    coordinate[i][j][3] = True
                    answer += 1
        elif x == "D":
            if j-1 >= 0:
                if coordinate[i][j][1] == True:
                    j -= 1
                else:
                    coordinate[i][j][1] = True
                    j -= 1
                    coordinate[i][j][0] = True
                    answer += 1
        elif x == "L":
            if i-1 >= 0:
                if coordinate[i][j][3] == True:
                    i -= 1
                else:
                    coordinate[i][j][3] = True
                    i -= 1
                    coordinate[i][j][2] = True
                    answer += 1    
    return answer
