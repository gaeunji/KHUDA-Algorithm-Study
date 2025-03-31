def solution(arr1, arr2):
    # 일단 두 matrix에 대해서 m x n 정의. (차원이 어떻게 되는지 체크)
    r1, c1 = len(arr1), len(arr1[0]) # r1은 arr1의 행 개수 m / c1 은 열 개수 n -> m x n
    r2, c2 = len(arr2), len(arr2[0])
    
    # 계산 결과를 저장할 matrix 정의. [r1 x c1] x [r2 x c2] -> r1 x c2
    answer = [[0]*c2 for _ in range(r1)] # c2가 열 개수임.
    
    # 이제 연산 작성
    # 일단 행 x 열 곱이니까, arr1의 행을 돌리면서 하나 고정 -> arr2의 열 돌리면서
    # -> arr1의 열 돌리면서 element wise로 곱하기
    # 즉, arr1[0] 이랑 arr2[0][0], arr2[1][0], arr2[2][0], ... 이렇게 곱하는거
    for i in range(r1): # 1. arr1의 행 돌리기
        for j in range(c2): # 2. arr2의 열 돌리기
            for k in range(c1): # 3. arr1의 열 돌리기
                answer[i][j] += arr1[i][k] * arr2[k][j] # 4. arr1 하나의 행과 arr2 하나의 열 곱하기
            
    return answer