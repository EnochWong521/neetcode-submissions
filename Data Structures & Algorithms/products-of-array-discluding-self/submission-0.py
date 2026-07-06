class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # iterate right to left then left to right 
        # example 1, 2, 4, 6
        # array 1: 1, 2, 8, 24
        # array 2: 6, 24, 48, 48
        # index 1 (i)
        # arr_1[i - 0 - 1] * arr_2[len(nums) - i - 2]
        left_arr = []
        right_arr = []
        
        for i in range(len(nums)):
            if i == 0:
                left_arr.append(nums[0]) 
            else: 
                left_arr.append(nums[i] * left_arr[i - 1])

        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                right_arr.append(nums[len(nums) - 1])
            else:
                right_arr.append(right_arr[len(nums) - j - 2] * nums[j])
        print(left_arr)
        print(right_arr)

        out_arr = []
        for k in range(len(nums)):
            if (k == 0):
                left = 1
            else:
                left = left_arr[k - 1]

            if (k == len(nums) - 1):
                right = 1
            else: 
                right = right_arr[len(nums) - k - 2]
            
            out_arr.append(left * right)

        return out_arr