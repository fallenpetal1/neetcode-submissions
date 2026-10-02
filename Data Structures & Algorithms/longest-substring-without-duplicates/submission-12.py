class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        charSet = set()

        for r in range(len(s)):
            while(s[r] in charSet):
                charSet.remove(s[l]) # Genius: Remove all chars till a specific char is                                     encountered. Remove s[l], not s[r]
                l+=1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res