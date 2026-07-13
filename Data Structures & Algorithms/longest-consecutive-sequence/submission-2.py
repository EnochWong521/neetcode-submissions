class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # use hash set 
        num_set = set(nums)
        max_seq = 0
        curr_seq = 1
        for n in num_set: 
            # determine where to start counting
            if n - 1 not in num_set: 
                start = n
                # count sequence
                while start + 1 in num_set: 
                    curr_seq += 1
                    start += 1
                # update max count
                if curr_seq > max_seq: 
                    max_seq = curr_seq
                curr_seq = 1
        return max_seq
        