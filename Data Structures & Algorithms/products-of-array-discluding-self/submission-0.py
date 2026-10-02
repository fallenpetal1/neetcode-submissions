class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf = [1] * len(nums), [1] * len(nums)
        l = len(nums)
        for i in range(l):
            if (i == 0):
                pre[i] = nums[i]
                suf[l-1-i] = nums[l-1-i]
            else:
                pre[i] = pre[i-1]*nums[i]
                if(i== l-1):
                    continue
                suf[l-1-i] = suf[l-i]*nums[l-1-i]

        fin = [1]*l
        for i in range(1, l-1):
            fin[i] = pre[i-1]*suf[i+1]
        fin[0] = suf[1]
        fin[l-1] = pre[l-2]
        return fin