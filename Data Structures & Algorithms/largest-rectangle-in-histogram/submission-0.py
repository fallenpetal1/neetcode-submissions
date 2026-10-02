class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        maxArea = 0

        for i, h in enumerate(heights):
            start = i
            while s and s[-1][1] > h:
                index, height = s.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index
            s.append((start, h))

        for i, h in s:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea