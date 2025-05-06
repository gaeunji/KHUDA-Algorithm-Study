# 첫 번째 행렬
n, m = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(n)]

# 두 번째 행렬
n2, m2 = map(int, input().split())
matrix2 = [list(map(int, input().split())) for _ in range(n2)]

result = [[0 for col in range(m2)] for row in range(n)]


for i in range(len(result)): # 행
    for j in range(m2): # 열
        sum = 0
        for k in range(m):
            sum += matrix1[i][k]*matrix2[k][j]

        result[i][j] = sum


for row in result:
    print(' '.join(map(str, row)))