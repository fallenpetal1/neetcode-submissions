class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers)-1
        for i in range(len(numbers)):
            if (numbers[p1] + numbers[p2] > target):
                p2 -= 1
                continue
            if (numbers[p1] + numbers[p2] < target):
                p1 += 1
                continue
            else:
                return [p1+1, p2+1]