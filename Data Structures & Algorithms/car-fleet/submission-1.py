import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p,s in zip(position, speed)]
        st = []

        for p, s in sorted(pair)[::-1]:
            noSteps = (target - p) / s
            if st and noSteps <= st[-1]:
                continue
            else:
                st.append(noSteps)
        return len(st)