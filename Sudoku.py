'''
Implementation of Solving a sudoku puzzle, code salvaged from pre-existing Sudoku Solver Gui
made by me. Available at https://github.com/Blakeinstein/Python-dev/tree/master/sudoku
Built using PyGame, and Python ofcourse.

The method of note here is Sudoku.solve, implemented using the backtracking algorithm, which 
backtracks if no possible solution exist for current node, and tries the next possibility 
for the previous node, and so on.

It is interesting to note that an unsolvable puzzle would remain and return unsolved.

I apologize for unprofessional comments.
'''
class Sudoku:
    '''
    The class Sudoku consists of the entire 9x9 board initialized with zeroes unless specified
    by passing a board arr of 9*9.
    '''
    def __init__(self, arr=[[0 for i in range(9)] for j in range(9)]):
        #as this is a simple proj, input is not error checked to be a 9*9 board but can be done
        self.arr = arr
        # the node property points to the current node being looked at
        self.node = [0, 0]

    def find(self):
        #The find function returns the next available empty spot on the board and sets the node
        # property to point to it. It also returns true in such a case. However if no such spot
        # is found, It doesnt alter the node property and returns false.
        for i in range(0, 9):
            for j in range(0, 9):
                if self.arr[i][j] == 0:
                    self.node[0] = i
                    self.node[1] = j
                    return True
        return False

    def ccr(self, row, num):
        #checks if the current num being tested is legible againsts the given row, returns boolean
        for i in range(0, 9):
            if self.arr[row][i] == num:
                return False
        return True

    def ccc(self, col, num):
        #checks if the current num being tested is legible againsts the given col, returns boolean
        for i in range(0, 9):
            if self.arr[i][col] == num:
                return False
        return True

    def ccb(self, row, col, num):
        #checks if the current num being tested is legible againsts the given box specified by the
        # most top right corner node of the box, returns boolean
        for i in range(3):
            for j in range(3):
                if self.arr[row + i][col + j] == num:
                    return False
        return True

    def check(self, row, col, num):
        #Checks if the current num satisfies the given board, by testing all conditions returns boolean
        return self.ccr(row, num) and self.ccc(col, num) and self.ccb(row - row%3, col - col%3, num)

    def solve(self):
        #Attempts to solve the board by using the Backtracking Algorithm.
        
        self.node = [0, 0] #clears current node being looked at
        
        if not self.find():
            return True #returns True if board has no empty space, ie the algorithm is done.
        
        # If an empty spot is found, all cases are tested against it, the row and column are then
        # extracted to their own variables
        row = self.node[0]
        col = self.node[1]
        
        #A loop is run to test all possible cases, if ever a wrong assumption is made, the 
        # loop falls back to the next possible value.
        for num in range(0, 10):
            #check if value satisfies, assign if it does or proceed to next value
            if self.check(row, col, num):
                self.arr[row][col] = num # assign value 
                #check if board can be solved, with the current value, this also makes a call for
                # the next empty spot to be solved for.
                if self.solve():
                    return True
                #if it cannot be solved with the current assignment, clear it and backtrack.
                self.arr[row][col] = 0
        #return false if board cannot be solved.
        return False

#Test code, this can however be imported as a module!
if __name__ == "__main__":
    #I dont remember where I found the board anymore, haha
    #I think it was a medium article about the hardest sudoku puzzle.
    #Too bad computers are op.
    BOARD = Sudoku([
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ])
    #Well edge cases are to be considered and well it was easy this time. OOF
    if(BOARD.solve()):
        print(BOARD.arr)
    else:
        print ("Board cannot be solved")
