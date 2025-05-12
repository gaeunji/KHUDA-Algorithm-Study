# 채점 결과: 실패
# 이유: 몰랑 ~

n = int(input()) # N
k = int(input()) # N^2 이하의 자연수


snail = [[0 for _ in range(n)] for _ in range(n)]


cur_row = n// 2
cur_col = n // 2
snail[cur_row][cur_col] = 1

direction = [(-1, 0), (0,1), (1,0), (0,-1)]

count = 1
idx = 0
num = 2

tpx = tpy = 0

while num <= n * n:
    for _ in range(2):  # 1, 2, 3,...이 2번씩 반복됨
        dy, dx = direction[idx]
        for _ in range(count):
            cur_row += dy
            cur_col += dx

            if 0 <= cur_row < n and 0 <= cur_col < n:
                snail[cur_row][cur_col] = num

                if num == k:
                    tpx = cur_row 
                    tpy = cur_col


                num += 1
        idx = (idx + 1) % 4
    count += 1
    



# ====== 출력 =======

for i in snail:
    for j in i:
        print(j, end=' ')
    print()

print(tpx + 1, tpy+ 1)
