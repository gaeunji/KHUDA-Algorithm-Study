n = int(input())
M = [[0 for _ in range(n)] for _ in range(n)]

x = int(input())
row, col = n//2, n//2
M[row][col] = 1
if x == 1:
    x_row, x_col = row, col

num = 2
step = 1

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while num <= n*n:
    for dir in range(4):
        for _ in range(step):
            if num > n*n:
                break
            row += dr[dir]
            col += dc[dir]
            M[row][col] = num
            if num == x:
                x_row, x_col = row, col
            num += 1
        if dir%2 == 1:
            step += 1

for nums in M:
    print(" ".join(map(str, nums)))
print(x_row + 1, x_col + 1)
