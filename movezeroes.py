def moveZeroes(self, nums: List[int]):
    '''
    Do not return anything, modify nums in-place instead.

    '''
    arr = []
    count_zero = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count_zero += 1
        else:
            arr.append(nums[i])
    for i in range(count_zero):
        arr.append(0)
    for i in range(len(arr)):
        nums[i] = arr[i]
    #Alternate Solution

    '''
        def moveZeroes(self, nums: List[int]) -> None:
            """
        Do not return anything, modify nums in-place instead.
        """
        nextIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[nextIndex] = nums[nextIndex],nums[i]
                nextIndex += 1
        return nums
    '''