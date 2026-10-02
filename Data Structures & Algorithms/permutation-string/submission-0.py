class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts1 = {}

        for i in range(len(s1)):
            counts1[s1[i]] = counts1.get(s1[i], 0) + 1

        l,r =0,0
        while (r<len(s2)):
            r = l + len(s1)
            s = s2[l:r]
            counts = {}
            l+=1
            for i in range(len(s)):
                counts[s[i]] = counts.get(s[i], 0) + 1
            if (counts == counts1):
                return True
            
        return False
        