class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        mapOfIndexAndNo = {}
        longest = 0
        for n in numset:
            if ((n-1) not in numset):
                l = 1
                c = n
                for j in range(len(numset)):
                    if c+1 in numset:
                        l += 1
                        c = c+1
                if longest < l:
                    longest = l

        return longest

