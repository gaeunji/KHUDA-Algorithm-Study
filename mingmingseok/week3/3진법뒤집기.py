def change(num,radix):
    if num==0 :
        return '0'
    nums = []
    while num :
        num, digit = divmod(num,radix)
        nums.append(str(digit))

    return ''.join(reversed(nums))

def solution(n):

    n1 = change(n,3)
    n1 = ''.join(reversed(n1))
    n1 = int(n1,3)
    return n1