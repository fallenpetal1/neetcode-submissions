class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tsl = []
        for i, a in enumerate(nums):
            if i > 0 and (nums[i] == nums[i-1]):
                continue
            l = i+1
            r = len(nums) - 1

            while l < r:
                if (a + nums[l] + nums[r] > 0):
                    r -= 1
                elif (a + nums[l] + nums[r] < 0):
                    l += 1
                else:
                    tsl.append([a, nums[l], nums[r]])
                    l+=1
                    while (nums[l-1] == nums[l] and l<r):
                        l += 1
        return tsl

        