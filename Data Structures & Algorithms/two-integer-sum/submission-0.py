class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for x in range(len(nums)): 
            # match found
            # lookup wants to be O(1) time complexity; 
            # other value I'm looking for has to be key
            # value corresponding will be index 
            if nums[x] in lookup: 
                idx1 = lookup[nums[x]]
                idx2 = x
                return [idx1, idx2]
            else: 
                lookup[target - nums[x]] = x

