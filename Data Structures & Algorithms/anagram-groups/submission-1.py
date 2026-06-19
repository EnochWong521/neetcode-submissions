class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make array for each string, that will be the key for lookup 
        # if there's a match, append to sub-list
        # if no match, create new list

        # key is array
        # strings are the value; value is a list 
        lookup = defaultdict(list)
        for s in strs:
            # build key for string
            key = [0] * 26
            for c in s: 
                idx = ord(c) - ord('a')
                key[idx] += 1
            # append to sub-list if key is already seen
            # if key not seen, create new sublist
            lookup[tuple(key)].append(s)
        
        return list(lookup.values())