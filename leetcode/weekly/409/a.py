from typing import List
class neighborSum:
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        self.dic = dict()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                value = grid[i][j]
                self.dic[value] = [i, j]
        self.n = len(grid)

    def adjacentSum(self, value: int) -> int:
        row = self.dic[value][0]
        col = self.dic[value][1]
        s = 0
        if row > 0:
            s += self.grid[row-1][col]
        if row < self.n-1:
            s += self.grid[row+1][col]
        if col > 0:
            s += self.grid[row][col-1]
        if col < self.n-1:
            s += self.grid[row][col+1]
        return s

    def diagonalSum(self, value: int) -> int:
        row = self.dic[value][0]
        col = self.dic[value][1]
        s = 0
        if row > 0 and col > 0:
            s += self.grid[row-1][col-1]
        if row < self.n-1 and col < self.n-1:
            s += self.grid[row+1][col+1]
        if row > 0 and col < self.n-1:
            s += self.grid[row-1][col+1]
        if row < self.n-1 and col > 0:
            s += self.grid[row+1][col-1]
        return s
    





# Your neighborSum object will be instantiated and called as such:
obj = neighborSum([[1, 2, 0, 3], [4, 7, 15, 6], [8, 9, 10, 11], [12, 13, 14, 5]])
param_1 = obj.adjacentSum(15)
# param_2 = obj.diagonalSum(value)