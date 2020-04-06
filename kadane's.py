def kadane(nums):
    start = sum = 0
    max_start = max_end = 0
    max_sum = float("-inf")
    for ind, value in enumerate(nums):
        if sum <= 0:
            start = ind
            sum = value
        else:
            sum += value
        if sum > max_sum:
            max_start = start
            max_end = ind
            max_sum = sum
    return max_start, max_end, max_sum




a = [1, 2, -4, 3, 4]
print(kadane(a))