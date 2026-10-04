class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums) - 1
        minI = 0
        while (l<=r):
            m = int((l+r)//2)
            if nums[m] < nums[minI]:
                minI = m
                r = m-1
            elif nums[m] >= nums[minI]:
                l = m+1
        return nums[minI]