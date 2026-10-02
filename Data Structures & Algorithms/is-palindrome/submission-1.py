class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns, rs = "", ""
        for i in range(len(s)):
            if (s[i].isalnum()):
                ns += s[i]
        for i in range(len(ns)-1, -1, -1): # Wrong: for i in range(len(ns)-1, 0, -1):
            rs += ns[i]
        return(ns.lower() == rs.lower()) #lower
