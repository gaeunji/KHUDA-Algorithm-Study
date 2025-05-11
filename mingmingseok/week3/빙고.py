import sys


bingo = []
for _ in range(5):
    input = sys.stdin.readline()
    bingo.append(input.split())



def checkbingo(bingo):
    #가로줄 체크
    bingo_count=0
    for i in range(5):
        if bingo[i] == [0,0,0,0,0]:
            bingo_count +=1
    #세로줄 체크
    for j in range(5):
        if bingo[0][j] == 0 and bingo[1][j] == 0 and bingo[2][j] == 0 and bingo[3][j] == 0 and bingo[4][j] == 0:
            bingo_count +=1

    #왼쪽 위부터 오른쪽 아래 체크
    if bingo[0][0] == 0 and bingo[1][1] == 0 and bingo[2][2] == 0 and bingo[3][3] == 0 and bingo[4][4] == 0:
        bingo_count +=1
    
    #오른쪽 위부터 왼쪽 아래 체크
    if bingo[4][0] == 0 and bingo[1][3] == 0 and bingo[2][2] == 0 and bingo[3][1] == 0 and bingo[4][0] == 0:
        bingo_count +=1

    if bingo_count >=3 :
        return True
    else :
        return False
call = []

for _ in range(5):
    input = sys.stdin.readline()
    call.append(input.split())

cnt = 0
while (True):
    call_number = call[cnt//5][cnt%5]
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == call_number:
                bingo[i][j] = 0
    
    if checkbingo(bingo):

        break
    cnt = cnt +1

print(cnt+1)
