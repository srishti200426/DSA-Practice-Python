class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        'transpose the matrix'
        for i in range(0,n-2+1):
            for j in range(i+1,n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        'reverse every row'

        for i in range(0,n):
            matrix[i].reverse()