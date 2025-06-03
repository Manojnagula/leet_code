class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return_array=[]
        for i in range(1,numRows+1):
            return_array.append([1]*i)
        for i in range(2,numRows):
            for j in range(1,i):
                return_array[i][j] = return_array[i-1][j-1]+return_array[i-1][j]
        return return_array