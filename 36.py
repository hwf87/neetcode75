# 36. Valid Sudoku
import collections
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        TC = O(9^2)
        SC = O(9)
        '''
        row_dict = collections.defaultdict(set)
        column_dict = collections.defaultdict(set)
        box_dict = collections.defaultdict(set)
        
        for r in range(0, 9):
            for c in range(0, 9):
                if board[r][c] == '.':
                    continue
                elif (
                    board[r][c] in row_dict[r] or
                    board[r][c] in column_dict[c] or
                    board[r][c] in box_dict[(r//3, c//3)]
                ):
                    return False
                else:
                    row_dict[r].add(board[r][c])
                    column_dict[c].add(board[r][c])
                    box_dict[(r//3, c//3)].add(board[r][c])
        return True

# Unit test
import pytest
class TestCase(Solution):
    @pytest.mark.parametrize("board, expect", \
                             [([["5","3",".",".","7",".",".",".","."]
                                ,["6",".",".","1","9","5",".",".","."]
                                ,[".","9","8",".",".",".",".","6","."]
                                ,["8",".",".",".","6",".",".",".","3"]
                                ,["4",".",".","8",".","3",".",".","1"]
                                ,["7",".",".",".","2",".",".",".","6"]
                                ,[".","6",".",".",".",".","2","8","."]
                                ,[".",".",".","4","1","9",".",".","5"]
                                ,[".",".",".",".","8",".",".","7","9"]], True),
                              ([["8","3",".",".","7",".",".",".","."]
                                ,["6",".",".","1","9","5",".",".","."]
                                ,[".","9","8",".",".",".",".","6","."]
                                ,["8",".",".",".","6",".",".",".","3"]
                                ,["4",".",".","8",".","3",".",".","1"]
                                ,["7",".",".",".","2",".",".",".","6"]
                                ,[".","6",".",".",".",".","2","8","."]
                                ,[".",".",".","4","1","9",".",".","5"]
                                ,[".",".",".",".","8",".",".","7","9"]],False)])
    def test_isValidSudoku(self, board, expect):
        '''
        '''
        answer = self.isValidSudoku(board)
        assert answer == expect