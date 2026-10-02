class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxH = 0
        for i in range(len(piles)):
            if piles[i] > maxH:
                maxH = piles[i]
        
        l = 1
        r = maxH
        minK = maxH
        while (l<=r):
            m = int((l+r)//2)
            tot = 0
            for i in range(len(piles)):
                tot += int(math.ceil(piles[i]/m))
            if (tot > h):
                l = m+1
            elif (tot <= h):
                minK = m
                r = m-1

        for j in range(l, minK):
            tot = 0
            for i in range(len(piles)):
                print(i)
                tot += int(math.ceil(piles[i]/j))
            print(tot)
            if (tot > h):
                    #print("continuing", tot)
                continue
            else:
                minK = j
                break


        return minK
        