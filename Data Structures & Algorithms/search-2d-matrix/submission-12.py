class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        ro = 0
        while i < len(matrix):
            if (matrix[i][0] > target):
                ro = i-1
                break
            if (matrix[i][0] == target):
                ro = i
                break
            ro = i
            i+=1

        l = 0
        r = len(matrix[ro])-1
        while (l<=r):
            m = int((l + r)// 2 )
            if target > matrix[ro][m]:
                l = m+1
            elif target < matrix[ro][m]:
                r = m-1
            else:
                return True
        return False
