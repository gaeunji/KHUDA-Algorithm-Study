def solution(num):
    if num == 0: return '0'

    nums = []
    while num:
        num, digit = divmod(num, 3)
        nums.append(str(digit))
    
    trit = "".join(nums)
    answer = int(trit, 3)
    
    
    return answer
