from pprint import pprint


def next_empty(puzzle):
    
    for r in range(9):
        for c in range(9): # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == 0:
                return r, c

    return None, None  # if no spaces in the puzzle are empty (0)

def is_valid(puzzle, guess, r, c):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False

    # for a guess to be valid, then we need to follow the sudoku rules
    # that number must not be repeated in the row, column, or 3x3 square that it appears in

    # let's start with the row
    row_vals = puzzle[r]
    if guess in row_vals:
        return False # if we've repeated, then our guess is not valid!

    # now the column
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][c] for i in range(9)]
    if guess in col_vals:
        return False

    # and then the square
    r_s = (r // 3) * 3 # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
    c_s = (c // 3) * 3

    for r in range(r_s, r_s + 3):
        for c in range(c_s, c_s + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
   
    r, c = next_empty(puzzle)

    if r is None: 
        return True 
    
    
    for guess in range(1, 10):
        if is_valid(puzzle, guess, r, c):
            
            puzzle[r][c] = guess
            
            if solve_sudoku(puzzle):
                return True
        
     
        puzzle[r][c] = 0

    
    return False  

if __name__ == '__main__':
    board = [
        [3, 9, 0,   0, 5, 0,   0, 0, 0],
        [0, 0, 0,   2, 0, 0,   0, 0, 5],
        [0, 0, 0,   7, 1, 9,   0, 8, 0],

        [0, 5, 0,   0, 6, 8,   0, 0, 0],
        [2, 0, 6,   0, 0, 3,   0, 0, 0],
        [0, 0, 0,   0, 0, 0,   0, 0, 4],

        [5, 0, 0,   0, 0, 0,   0, 0, 0],
        [6, 7, 0,   1, 0, 5,   0, 4, 0],
        [1, 0, 9,   0, 0, 0,   2, 0, 0]
    ]
    print(solve_sudoku(board))
    pprint(board)
