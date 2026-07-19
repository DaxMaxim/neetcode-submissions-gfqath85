class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1

        while l <= r:
            mid = (l+r)//2
            
            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[0])-1]:
                break
            elif target > matrix[mid][len(matrix[0])-1]:
                l = mid + 1
            else:
                r = mid - 1 
        
        l, r = 0, len(matrix[0]) - 1

        while l <= r:
            m = (l + r)//2

            if matrix[mid][m] == target:
                return True
            elif target > matrix[mid][m]:
                l = m + 1
            else:
                r = m - 1
        return False