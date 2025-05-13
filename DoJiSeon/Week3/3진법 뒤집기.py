def solution(n):
    answer = 0
    answer = radixChange(n, 3)
    reverse = answer[::-1]
    answer = int(reverse,3)
    return answer

def radixChange(num, radix):
    if num == 0:
            return '0'
    nums = []
    while num:
            num, digit = divmod(num, radix)
            nums.append(str(digit))
    return "".join(reversed(nums))