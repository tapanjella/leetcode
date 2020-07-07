'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
'''
def twoSum(self, nums: List[int], target: int) -> List[int]:
    list1 = []
    dict1 = {} # mapping element to its index ele:index
    for index,ele in enumerate(nums):
        val = target - ele
        if val in dict1:
            list1.append(index)
            list1.append(dict1[val])
            return list1
        else:
            dict1[ele] = index
