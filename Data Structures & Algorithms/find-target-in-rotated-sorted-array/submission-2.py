class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        minI = 0
        while (l<=r):
            m = int((l+r)//2)
            if (nums[m] < nums[minI]):
                minI = m
                r = m-1
            elif (nums[m] >= nums[minI]):
                l = m+1
        if minI == 0:
            l = 0
            r = len(nums) - 1
        elif target < nums[0]:
            l = minI
            r = len(nums) - 1
        elif target > nums[0]:
            l = 0
            r = minI - 1
        else: 
            return 0
        while (l<=r):
            m = int((l+r)//2)
            if (nums[m] < target):
                l = m+1
            elif(nums[m] > target):
                r = m-1
            else:
                return m
        return -1
