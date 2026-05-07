class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            
            t, b = 0, len(matrix) - 1

            while t <= b:
                mid = (t + b) // 2
                l,r = 0, len(matrix[0]) - 1
                if matrix[mid][0] > target:

                    b = mid - 1
                elif matrix[mid][0] < target:
                    while l <= r:
                        mid_row = (l + r) // 2
                        if matrix[mid][mid_row] > target:
                            r = mid_row - 1
                        elif matrix[mid][mid_row] < target:
                            l = mid_row + 1
                        else:
                            return True
                    t = mid + 1

                else:
                    return True 
            return False

