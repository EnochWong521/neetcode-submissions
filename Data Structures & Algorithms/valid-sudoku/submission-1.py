class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1: check the current horizontal array for duplicates
        # 2: check vertical array 
        # 3: check sub-box

        # 1 + 2: 
        h_seen = set()
        v_seen = set()
        box_seen = set()
        for i in range(9):
            for j in range(9):
                row_val = board[i][j]
                col_val = board[j][i]
                if row_val != '.':
                    box_val = (i // 3, j // 3, row_val)
                    if row_val in h_seen:
                        return False
                    if box_val in box_seen:
                        return False 
                    h_seen.add(row_val)
                    box_seen.add(box_val)
                if col_val != '.':
                    if col_val in v_seen:
                        return False
                    v_seen.add(col_val)
            h_seen.clear()
            v_seen.clear()
        return True



