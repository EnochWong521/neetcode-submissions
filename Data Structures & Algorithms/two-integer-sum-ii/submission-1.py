class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # idx1 = 0
        # idx2 = len(numbers) - 1
        # if num[idx1] + num[idx2] > target: idx2--
        # elif < target idx1++
        idx1 = 0
        idx2 = len(numbers) - 1
        while (idx1 < idx2):
            curr_sum = numbers[idx1] + numbers[idx2]
            if curr_sum == target: 
                return [idx1 + 1, idx2 + 1]
            elif curr_sum > target: 
                idx2 -= 1
            else:
                idx1 += 1