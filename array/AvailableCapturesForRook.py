# LC 999
class Solution:
    def numRookCaptures(self, board):
        height = len(board)
        width = len(board[0])
        R_i, R_j = self.get_rook(height, width, board)
        directions = {}
        directions['up'] = [-1, 0]
        directions['down'] = [1, 0]
        directions['left'] = [0, -1]
        directions['right'] = [0, 1]
        result = 0
        for d in directions:
            i, j = R_i, R_j
            while 0 <= i < height and 0 <= j < width:
                i += directions[d][0]
                j += directions[d][1]
                if 0 <= i < height and 0 <= j < width:
                    if board[i][j] == "p":
                        result += 1
                        break
                    elif board[i][j] == "B":
                        break
        return result

    def get_rook(self, height, width, board):
        for i in range(height):
            for j in range(width):
                if board[i][j] == "R":
                    return i, j


if __name__ == "__main__":
    board = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]
    for l in board:
        print(l)
    print(Solution().numRookCaptures(board))
