class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        # matrix is just a sorted array 
        left, right = 0, ROWS * COLS - 1
        while left <= right:
            mid = (left + right) // 2 
            # row number is the division between mid index and number of num in each row(COLS)
            # col number is the remainder of above division
            row, col = mid // COLS, mid % COLS
            if matrix[row][col] < target:
                left += 1 
            elif matrix[row][col] > target:
                right -= 1
            else:
                return True 
        
        return False