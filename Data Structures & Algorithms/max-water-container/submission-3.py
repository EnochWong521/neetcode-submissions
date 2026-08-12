class Solution:
    def maxArea(self, heights: List[int]) -> int:
        last = len(heights) - 1
        water = 0
        max1 = 0
        max2 = last
        while max1 < max2:
            w = max2 - max1
            if heights[max1] < heights[max2]:
                h = heights[max1]
                max1 += 1
            else: 
                h = heights[max2]
                max2 -= 1
            curr = h * w
            if curr > water:
                water = curr
        return water
            