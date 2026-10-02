class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for str in strs:
            count = [0] * 26 # declare
            for c in str:
                count[ord(c) - ord('a')] += 1 # ord logic
            res[tuple(count)].append(str) # List / Array cannot be a key. Convert to tuple (immutable / hashable)

        return list(res.values())