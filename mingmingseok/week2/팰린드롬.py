T = int(input())

def check(str):
    arr = []
    str_word = list(str)
    str_word.reverse()
    str_word = "".join(str_word)
    if str == str_word:
        return True



for _ in range(T):

    swtich = False
    k = int(input())
    arr = []
    for _ in range(k):
        arr.append(input())

    arr_p =[]

    for i in range(k):
        for j in range(k):
            if i!=j:
                arr_p.append(arr[i]+arr[j])


    for k in arr_p:
        if check(k):
            swtich = True
            print(k)
            break
    if swtich == False : 
        print(0)
    


