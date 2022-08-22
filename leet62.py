class Solution:
    def UniquePaths(self,m,n):
        row = [1]*n
        for i in range(m-1):
            newRow = [1]*n
            for j in range(n-2,-1,-1):
                newRow[j] = newRow[j+1]+row[j]
            row = newRow
        return row[0]

a = Solution()
print(a.UniquePaths(7,3))