class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # iterate right to left then left to right 
        # example 1, 2, 4, 6
        # array 1: 1, 2, 8, 48
        # array 2: 6, 24, 48, 48
        # result: 48, 24, 12, 8
        # index 1 (i)
        # arr_1[i - 0 - 1] * arr_2[len(nums) - i - 2]
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
            

        return res