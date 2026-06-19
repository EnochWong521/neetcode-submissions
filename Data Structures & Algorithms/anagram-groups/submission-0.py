class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make array for each string, that will be the key for lookup 
        # if there's a match, append to sub-list
        # if no match, create new list

        # key is array
        # strings are the value; value is a list 
        lookup = {}
        anagram = []
        for s in strs:
            # build key for string
            key = [0] * 26
            for c in s: 
                idx = ord(c.upper()) - ord('A')
                key[idx] += 1
            key = tuple(key)
            # append to sub-list if key is already seen
            if key in lookup:
                lookup[key].append(s)
            # if key not seen, create new sublist
            else:
                lookup[key] = [s]
        
        # build output list
        for l in lookup.values():
            anagram.append(l)
        return anagram