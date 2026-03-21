class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        sr, sc = 0,0
        er, ec = m-1, n-1
        while sr<=er and sc<=ec:
            mr,mc = sr+er+1//2, sc+ec+1//2
            if target == matrix[mr][mc]:
                return True
            elif target>matrix[mr][mc]:
                sc = mc+1
            elif target<matrix[mr][mc]:
                if target<matrix[mr][0]:
                    er = mr-1
                else:
                    ec = mc - 1
        return False