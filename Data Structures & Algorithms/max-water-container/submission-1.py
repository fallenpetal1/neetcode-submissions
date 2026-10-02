class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1
        ar = 0
        while l<r:
            area = abs(l-r)*min(heights[l], heights[r])
            if (area>ar):
                ar = area
            if (heights[r] < heights[l]):
                r-=1
            elif (heights[l] <= heights[r]):
                l+=1
        
        return ar