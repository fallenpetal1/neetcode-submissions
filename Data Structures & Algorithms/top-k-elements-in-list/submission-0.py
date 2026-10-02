from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for num in nums:
            res[num] += 1
        sortd = dict(sorted(res.items(), key = itemgetter(1), reverse=True))
        return list(sortd.keys())[:k]