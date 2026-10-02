from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for num in nums:
            res[num] += 1
        # sortd = dict(sorted(res.items(), key = itemgetter(1), reverse=True)) # might be difficult to remember the function.. so alternate / original soln
        # return list(sortd.keys())[:k]
        arr = [[] for i in range(len(nums) + 1)]
        for ke, v in res.items():
            arr[v].append(ke)
        
        res = []
        for i in range(len(arr) - 1, 0, -1):
            for n in arr[i]:
                res.append(n)
        
        return res[:k]
        