def pallindrome(str_list):
    for i in range(len(str_list)):
        for j in range(len(str_list)):
            if i != j:
                original = str_list[i]+str_list[j]
                new_str = list(original) # "aaba"+"ba" ["a", "a", "b", "a"]+["b", "a"]
                new_str.reverse()
                str = "".join(new_str)
                if original == str:
                    return str
    return 0

t = int(input())
for i in range(t):
    k = int(input())
    str_list = []
    for j in range(k):
        str_list.append(input())
    print(pallindrome(str_list))
