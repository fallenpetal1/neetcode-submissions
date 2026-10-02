class Solution:
    @staticmethod
    def isUniqueAndValid(row: List[str]):
        arr = []
        for s in row:
            if (s == '.'):
                continue
            if s in arr:
                return False
            arr.append(s)
        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isUniqueAndValid(board[i]):
                return False
        for i in range(9):
            col = ['.'] * 9
            for j in range(9):
                col[j] = board[j][i]
                if not self. isUniqueAndValid(col):
                    return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                arr = ['.'] * 9
                c = 0
                for k in range(i, i+3, 1):
                    for l in range(j, j+3, 1):
                        arr[c] = board[k][l]
                        c += 1
                if not self. isUniqueAndValid(arr):
                    return False

        return True



        