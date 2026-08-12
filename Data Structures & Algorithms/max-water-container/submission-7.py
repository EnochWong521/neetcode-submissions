class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        ptr1 = 0
        ptr2 = len(heights) - 1
        while ptr1 < ptr2:
            w = ptr2 - ptr1
            if heights[ptr1] < heights[ptr2]:
                h = heights[ptr1]
                ptr1 += 1
            else: 
                h = heights[ptr2]
                ptr2 -= 1
            curr = h * w
            if curr > water:
                water = curr
        return water
            