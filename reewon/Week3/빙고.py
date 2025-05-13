bingo = [list(map(int, input().split())) for _ in range(5)]

# 사회자의 숫자 입력을 list in list가 아닌 하나의 list로 생성
call = []
for _ in range(5):
    ls = list(map(int, input().split()))
    call.extend(ls)

# 중복 카운트 방지를 위한 집합
completed_rows = set()
completed_cols = set()
completed_diagonals = set()
bingo_cnt = 0

# 빙고 조건 충족 여부 확인
def is_bingo_row(row):
    return all(x == 0 for x in bingo[row])

def is_bingo_col(col):
    return all(bingo[i][col] == 0 for i in range(5))

def is_bingo_diag1():
    return all(bingo[i][i] == 0 for i in range(5))

def is_bingo_diag2():
    return all(bingo[i][4-i] == 0 for i in range(5))

for idx, number in enumerate(call):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == number:
                bingo[i][j] = 0

                if i not in completed_rows and is_bingo_row(i):
                    completed_rows.add(i)
                    bingo_cnt += 1
                
                if j not in completed_cols and is_bingo_col(j):
                    completed_cols.add(i)
                    bingo_cnt += 1

                if i == j and "diag1" not in completed_diagonals and is_bingo_diag1():
                    completed_diagonals.add("diag1")
                    bingo_cnt += 1
                
                if i + j == 4 and "diag2" not in completed_diagonals and is_bingo_diag2():
                    completed_diagonals.add("diag2")
                    bingo_cnt += 1

                break
    if bingo_cnt >= 3:
        print(idx + 1)
        break    
