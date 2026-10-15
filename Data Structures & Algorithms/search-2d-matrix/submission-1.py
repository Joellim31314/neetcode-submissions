class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix)-1
        while start <= end:
            mid = (end + start)//2
            if target > matrix[mid][-1]:
                start = mid + 1
            elif target < matrix[mid][0]:
                end = mid- 1  
            else:
                break
        if start > end:
            return False
        row = (start + end)//2
        l = 0 
        r = len(matrix[mid])-1
        while l <=r:
            m = (r+l)//2
            if target > matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m-1
            else:
                return True
        return False

