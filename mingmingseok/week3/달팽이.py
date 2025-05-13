import sys
input = sys.stdin.readline

N = int(input())
target = int(input())

matrix = [[0]*N for _ in range(N)]
top, bottom = 0, N-1
left, right = 0, N-1
num = N * N

res_row = res_col = 0

while top <= bottom and left <= right:

    for i in range(top, bottom+1):
        matrix[i][left] = num
        if num == target:
            res_row, res_col = i+1, left+1
        num -= 1
    left += 1


    for j in range(left, right+1):
        matrix[bottom][j] = num
        if num == target:
            res_row, res_col = bottom+1, j+1
        num -= 1
    bottom -= 1


    if left <= right:
        for i in range(bottom, top-1, -1):
            matrix[i][right] = num
            if num == target:
                res_row, res_col = i+1, right+1
            num -= 1
        right -= 1


    if top <= bottom:
        for j in range(right, left-1, -1):
            matrix[top][j] = num
            if num == target:
                res_row, res_col = top+1, j+1
            num -= 1
        top += 1

# 출력
for row in matrix:
    print(*row)
print(res_row, res_col)
