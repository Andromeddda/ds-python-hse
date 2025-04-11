def twoSum(nums, target):
    d = dict()
    for i, n in enumerate(nums):
        if n in d:
            return [d[n], i]
        d[target - n] = i 

    return []

print(twoSum([2, 7, 11, 15], 9))