from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # INITIAL IDEA
        # we go through each row in a loop
        # check if the values are in the set, add if not, check if it is
        # if duplicate invalid sudoku
        # don't have to loop through anything else if found invalid

        # we go through each column in a loop
        
        #set is made each row


        #separate loops doesnt cover the square checks, so you need a nested loop
        # figure out how each square is grouped together
        #
        # finish check 1 square i + 2 (or 3)
        # increment i so that it checks the next square

        # after checking the 3 squares in the row, then you want to iterate the coliumns 

        #IDEA AFTER HINT
        # Create a hashmap to store rows, columns, and squares
        # If row is already in the hashmap, then it is invalid
        # etc. for column and squares

        #row = {}
        #column = {}
        #squares = {}
        row = defaultdict(set)
        column = defaultdict(set)
        squares = defaultdict(set)

        for i in range(9):
            print(board[i])
            for j in range(9):
                if (board[i][j] in row[i] or board[i][j] in column[j] or board[i][j] in squares[(i // 3, j // 3)]):
                    return False
                if (board[i][j] == '.'):
                    continue
                #row[i] = board[i][j]
                row[i].add(board[i][j])
                column[j].add(board[i][j])
                # FROM HINT 3: (row / 3) * 3 + (col / 3)
                #squares[(i / 3) * 3 + (j / 3)].add(board[i][j]) WRONG
                # we use floor division, to group each of the quadrants
                squares[(i // 3, j // 3)].add(board[i][j])
        print(row[0])
        print(column[0])
        print(squares[(0, 0)])
        return True
    
solution = Solution()
case1 = [["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]
print('Output: ', solution.isValidSudoku(case1))