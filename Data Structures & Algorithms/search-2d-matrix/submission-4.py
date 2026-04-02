class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # matrix is essentially a sorted array 
        ROWS, COLS = len(matrix), len(matrix[0])
        # right is last element of matrix
        left, right = 0, ROWS*COLS - 1
        while left <= right:
            mid = left + (right - left) // 2
            # row is array mid index divide by col number(len of each sub array)
            # col is remainder of division above 
            row, col = mid // COLS, mid % COLS
            if matrix[row][col] > target:
                right = mid - 1
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                return True 
        
        return False 