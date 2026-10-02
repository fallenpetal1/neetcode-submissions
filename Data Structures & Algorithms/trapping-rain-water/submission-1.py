class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight = [0]*len(height), [0]*len(height)
        maxL, maxR = 0, 0
        for i in range(len(height)):
            maxLeft[i] = maxL
            if (height[i] > maxL):
                maxL = height[i]

        for i in range(len(height)-1, -1, -1):
            maxRight[i] = maxR
            if (height[i] > maxR):
                maxR = height[i]

        vol = 0
        for i in range(len(height)):
            v = min(maxLeft[i], maxRight[i]) - height[i]
            if (v > 0):
                vol += v
        return vol