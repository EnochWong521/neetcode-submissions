class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0
        ptr1 = 0
        ptr2 = len(heights) - 1
        while ptr1 < ptr2:
            width = ptr2 - ptr1
            height = min(heights[ptr1], heights[ptr2])
            water = max(water, height * width)
            if heights[ptr1] < heights[ptr2]:
                ptr1 += 1
            else: 
                ptr2 -= 1
        return water
            