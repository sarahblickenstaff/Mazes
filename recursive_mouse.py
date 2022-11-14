''' 
    Class Mouse contains the recursive solutions to a given Maze object, bounded by up, down, left, and right movement.
    It will print all possible solutions. 
'''

from pyliststack import *
from maze import *

class Mouse:

    def __init__(self):
        ''' The mouse keeps track of how many times it finds a solution to the maze
        '''
        self.solutions = 0

    def findMazePaths(self, maze, startRow, startCol, exitRow, exitCol):
        ''' Searches for the exit path of the maze and explores the four neighbors of the current position by calling exploreFourNeighbors
        '''
        col = startCol
        row = startRow

        if col == exitCol and row == exitRow:   #The exit is found!
            maze.setValue(row, col, '!')
            print("success!")
            print(maze)                         #Print the solution to the maze
            self.solutions += 1
            return

        elif self.checkValid(maze, row, col):
            self.exploreFourNeighbors(maze, row, col, exitRow, exitCol)
            
        else:
            print("Invalid row/col")
            return


    def exploreFourNeighbors(self, maze, row, col, exitRow, exitCol):
        ''' Checks for vaild neighbors of the current position and recursively calls findMazePaths 
        '''

        maze.setValue(row, col, '!')
        maze = copy.deepcopy(maze)      #Create deep copy of maze with path marked

        #Check up
        if self.checkValid(maze, row - 1, col):
            self.findMazePaths(maze, (row - 1), col, exitRow, exitCol)
        #Check down
        if self.checkValid(maze, row + 1, col):
            self.findMazePaths(maze, (row + 1), col, exitRow, exitCol)
        #Check right
        if self.checkValid(maze, row, col - 1):
            self.findMazePaths(maze, row, (col - 1), exitRow, exitCol)
        #Check left
        if self.checkValid(maze, row, col + 1):
            self.findMazePaths(maze, row, (col + 1), exitRow, exitCol)

    def checkValid(self, matrix, row, col):
        ''' Returns true if the current position has not already been checked and is not a wall
        '''
        return matrix.isClear(row, col) and matrix.isInMaze(row, col)
