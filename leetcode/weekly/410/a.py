class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i, j = 0, 0
        operations = {
            "RIGHT": [0, 1],
            "DOWN": [1, 0],
            "LEFT": [0, -1],
            "UP": [-1, 0]
        }
        for c in commands:
            ops = operations[c]
            i += ops[0]
            j += ops[1]
        return (i * n) + j
            