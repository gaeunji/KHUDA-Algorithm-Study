import sys
player = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
host = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

def find(item):
    for i in range(5):
        for j in range(5):
            if item == player[i][j]:
                player[i][j] = 0
                return

def check():
    line = 0
    row_sum = 0
    col_sum = 0
    for i in range(5):
        row_sum = 0
        col_sum = 0
        for j in range(5):
            row_sum = row_sum + player[i][j]
            col_sum = col_sum + player[j][i]
        if row_sum == 0:
            line = line+ 1
        if col_sum == 0:
            line = line + 1
    
    left_cross = 0
    right_cross = 0
    for j in range(5):
        left_cross += player[j][j]
        right_cross += player[j][4-j]

    if left_cross == 0:
        line = line + 1
    if right_cross == 0:
        line = line + 1
    return line


count = 0
for i in range(5):
    for j in range(5):
        num = host[i][j]
        find(num)

        count = count + 1
        if check() >= 3:
            print(count)
            sys.exit()

    
