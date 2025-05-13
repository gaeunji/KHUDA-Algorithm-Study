import sys

n = int(input())
point = int(input())
array = [[0 for col in range(n)] for row in range(n)]
point_answer = []

def print_matrix():
    for i in range(n):
        print(' '.join(map(str, array[i])))
    print(point_answer[0]+1, point_answer[1]+1)

row = n//2
col = n//2
array[row][col] = 1
if point == 1:
    point_answer.append(row)
    point_answer.append(col)
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 오른쪽 아래 왼쪽 위 순으로 뱅글뱅글

row += -1 # 왼쪽위쪽으로 기본적으로 -1,-1칸 옮겨주고 시작
col += -1
count = 2
# 2 4 6씩 증가해야함
for i in range(2, n , 2):
    for j in range(i * 4):
        row += direction[j//i][0]
        col += direction[j//i][1]
        array[row][col] = count
        if count == point:
            point_answer.append(row)
            point_answer.append(col)
        count +=1
    row += -1
    col += -1

print_matrix()