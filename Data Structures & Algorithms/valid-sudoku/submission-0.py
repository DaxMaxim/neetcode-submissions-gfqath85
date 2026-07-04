class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = defaultdict(set)

        for i in range(9):
            curr_row, curr_col = set(), set()

            for j in range(9):

                if board[i][j] in curr_row or board[j][i] in curr_col: 
                    return False
                if board[i][j] in boxes[(i//3, j//3)]:
                    return False
                
                if board[i][j] != ".": 
                    curr_row.add(board[i][j])
                    boxes[(i//3, j//3)].add(board[i][j])
                if board[j][i] != ".": curr_col.add(board[j][i])
        return True


        
                