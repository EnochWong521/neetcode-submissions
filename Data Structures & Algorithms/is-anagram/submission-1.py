class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = {}
        # lookup table for string 1
        for i in s: 
            if i in str1:
                str1[i] += 1
            else:
                str1[i] = 1

        # check character matching with string 2
        for j in t: 
            # decrement count if seen
            if j in s: 
                str1[j] -= 1
            # return false if character mismatch
            else:
                return False

        # final check for if all characters have been matched
        for k in s:
            if str1[k] != 0:
                return False
        
        return True
