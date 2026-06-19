class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep hash maps of frequencies of each number 
        # after hash map is built, how to find k most unique? 
        # array to indexed by frequency corresponding to list of numbers
        num_to_freq = {}
        # build hash map
        for n in nums:
            # if seen increment frequency by 1
            num_to_freq[n] = num_to_freq.get(n, 0) + 1
        
        # build frequency array
        arr = [[] for x in range(len(nums) + 1)]
        for num, freq in num_to_freq.items():
            # index = frequency 
            # value = number
            # append to sublist
            arr[freq].append(num)
        # find top k elements
        cnt = k
        res = []
        # iterate from highest to lowest frequency
        # idx 0 1 2 3
        # val / 1 2 3
        for freq in range(len(nums), 0, -1):
            for num in arr[freq]:
                res.append(num)
                if len(res) == k: 
                    return res