class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        a = 0
        for i in range(len(tokens)):
            if tokens[i] == "+":
                l = st.pop()
                f = st.pop()
                a = int(f) + int(l)
                st.append(a)
            elif (tokens[i] == "-"):
                l = st.pop()
                f = st.pop()
                a = int(f) - int(l)
                st.append(a)
            elif (tokens[i] == "*"):
                l = st.pop()
                f = st.pop()
                a = int(l) * int(f)
                st.append(a)
            elif (tokens[i] == "/"):
                l = st.pop()
                f = st.pop()
                a = int(int(f) / int(l))
                st.append(a)
            else:
                st.append(tokens[i])
        return int(st[-1])