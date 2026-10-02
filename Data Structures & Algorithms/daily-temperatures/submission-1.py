class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while(st and t > st[-1][1]):
                stInd, stTemp = st.pop()
                res[stInd] = i - stInd
            st.append([i, t])
        return res            
