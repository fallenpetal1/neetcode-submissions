class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        brackets = {"]" : "[", 
                    "}" : "{",
                    ")" : "("}
        for i in range(len(s)):
            if s[i] in ["[", "{", "("]:
                st.append(s[i])
            elif s[i] in ["]", "}", ")"]:
                #print(st, st.pop(), brackets.get(s[i]))
                if not st:
                    return False
                if(st and st.pop() != brackets.get(s[i])):
                    return False
        if st:
            return False
        return True
                