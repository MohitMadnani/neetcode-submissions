class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        correct_row = -1
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                correct_row = i

        if correct_row == -1:
            return False

        low = 0
        high = len(matrix[correct_row]) - 1

        while low <= high:
            mid = low + (high - low) // 2
            midv = matrix[correct_row][mid]

            if midv == target:
                return True
            elif midv < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False



        