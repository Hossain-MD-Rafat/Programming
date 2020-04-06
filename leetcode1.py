def singleNumber(nums) -> int:
    num = nums[0]
    n = len(nums)
    for i in range(1,n):
        num = num ^ nums[i]
    return num
num = 96
num = num ^ 8
num = num ^ 7
num1 = 96 ^ 3
print(num1 ^ 3)
print(num)

print(singleNumber([1,2,3,2,1]))