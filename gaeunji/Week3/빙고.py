import sys


def check_bingo(arr):
    bingo = 0
    
    # 2차원 배열의 1 ~ 5번째 행
    for row in arr:
        if all (a[1] == 1 for a in row):
            bingo += 1

    # len(arr): 행의 개수, len(arr[i]): 열의 개수 
    # arr[j][i] = i행 j열, i+1행 j열, ...
    for i in range(len(arr)):
        if all(arr[j][i][1] == 1 for j in range(len(arr[i]))):
            bingo += 1
            
    
    if all(arr[i][i][1] == 1 for i in range(5)):
        bingo += 1
    
    if all(arr[i][4 - i][1] == 1 for i in range(5)):
        bingo += 1

    return bingo



# 임의의 개수의 정수를 n줄 입력받아 2차원 리스트에 저장
data = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

arr = [[(num, 0) for num in row] for row in data]

count = 0
answer = 0

nums = []
for _ in range(5):
    nums += list(map(int, sys.stdin.readline().split()))

for num in nums:
    count += 1
    for i in range(5):
        for j in range(5):
            if arr[i][j][0] == num:
                arr[i][j] = (num, 1)
    if count >= 12:
        res = check_bingo(arr)
        if res >= 3:
            print(count)
            break

