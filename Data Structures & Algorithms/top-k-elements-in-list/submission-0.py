class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep hash maps of frequencies of each number 
        # after hash map is built, how to find k most unique? 
        # array to indexed by frequency corresponding to list of numbers
        num_to_freq = {}
        for n in nums:
            # increment occurrence by 1 if seen 
            if n in num_to_freq: 
                num_to_freq[n] += 1
            # create new key if not seen
            else:
                num_to_freq[n] = 1
        
        # build frequency array
        arr = [[] for x in range(len(nums) + 1)]
        for key in num_to_freq:
            # index = frequency 
            idx = num_to_freq[key]
            # value = number
            # append to sublist
            arr[idx].append(key)
        # find top k elements
        cnt = k
        res = []
        # iterate from highest to lowest frequency
        # idx 0 1 2 3
        # val / 1 2 3
        for x in range(len(nums), 0, -1):
            # flush sub-array
            while (cnt > 0 and arr[x]):
                val = arr[x].pop()
                res.append(val)
                cnt -= 1

        return res