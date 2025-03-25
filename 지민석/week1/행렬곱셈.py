

N,M = map(int,(input().split()))

A = [[0 for _ in range (M)] for _ in range(N)]

for i in range (N):
    A[i] = list(map(int,input().split()))
    




M,K = map(int,(input().split()))

B = [[0 for _ in range (K)] for _ in range(M)]

for i in range (M):
    B[i] = list(map(int,input().split()))


answer = [[0 for _ in range(K)] for _ in range (N)]

for i in range (N):
    for j in range(K):
        ##행렬A에서는 i번째 행, 행렬 B에서는 i번째 열과 곱곱
        for k in range(M):
            answer[i][j] = answer[i][j]+A[i][k]*B[k][j]


for i in range(N):
    for j in range(K):
        print(answer[i][j], end = ' ')
    print()
