def palindrome():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    
    arr_len = len(arr)
    for i in range(arr_len):
        for j in range(arr_len):
            if i!=j:
                word = arr[i] + arr[j]
                if word == word[::-1]:
                    return word
                
    return 0

t = int(input())  # 사용자로부터 테스트 케이스의 개수를 입력받아 변수 t에 저장
                  # input() 함수는 사용자로부터 입력을 받음. 그러나 입력은 문자열이기에, 정수로 변환.
                  # t는 테스트 케이스의 개수를 의미함
                  #            
while t > 0:  # t가 0보다 클 동안 반복    
    ans = palindrome()  # palindrome() 함수의 결과를 ans에 저장
    print(0) if ans == 0 else print(ans)  # ans가 0이면 0을 출력, 아니면 ans 값을 출력
    t -= 1  # t의 값을 1 감소시켜, t가 0이 될때 프로그램을 종료함
