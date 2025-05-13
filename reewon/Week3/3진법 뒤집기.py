def radixChange(num, radix):
    if num == 0: return 0
    nums = []
    while num:
        num, digit = divmod(num, radix)
        nums.append(str(digit))
    return "".join(nums)
    
def solution(n):
    n = radixChange(n, 3)
    answer = int(str(n), 3)
    return answer
