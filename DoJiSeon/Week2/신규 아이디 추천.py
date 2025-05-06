def solution(new_id):
    id = new_id.lower() # 1
    special = ['-', '_', '.']

    arr = []
    for item in id: # 2
        if item.isalnum() == False:
            if item in special:
                arr.append(item)
        else:
            arr.append(item)
    
    popped = []
    for i in range(1, len(arr)):
        if arr[i-1] == '.' and arr[i] == '.':
            popped.append(i)
    
    popped.reverse()
    for item in popped:
        arr.pop(item) #3

    if len(arr) != 0 and arr[0] == '.': #4
        arr.pop(0)

    if len(arr) != 0 and arr[-1] == '.':#4
        arr.pop(-1)
    
    if len(arr) == 0:
        arr.append("a")

    context = "".join(arr)

    if len(context) > 15: # 6
        context = context[:15] 
        arr = list(context)
        if len(arr) != 0 and arr[0] == '.': #4
            arr.pop(0)

        if len(arr) != 0 and arr[-1] == '.':#4
            arr.pop(-1)

        answer = "".join(arr)
        return answer
    elif len(context) <= 2: # 7
        while(len(arr) != 3):
            arr.append(arr[len(arr)-1])

    answer = "".join(arr)
    return answer