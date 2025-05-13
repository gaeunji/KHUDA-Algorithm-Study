#[4,2,2,1,3,4]
def result_function(arr1):
    arr1.sort()
    print(arr1)

    list1 = []
    for i in range(len(arr1)):
        arr_length = len(arr1)
        if i < arr_length-1:
            if arr1[i] != arr1[i+1]:
                list1.append(arr1[i]) 
        elif i == arr_length-1:
            list1.append(arr1[i])
    return list1
