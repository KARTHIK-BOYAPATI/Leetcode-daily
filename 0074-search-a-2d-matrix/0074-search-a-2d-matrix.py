class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        top = 0 
        bottom = rows - 1
        left = 0 
        right = columns - 1
        row = 0
        while(top<=bottom):
            mid = (top+bottom)//2
            if(matrix[mid][-1]>=target):
                row = mid
                bottom = mid-1
            else:
                top = mid+1
                
        while(left<=right):
            mid = (left+right)//2
            if(matrix[row][mid]==target):
                return True
            elif (matrix[row][mid] > target):
                right = mid-1
            else:
                left = mid+1
        return False
                
                