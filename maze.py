"""
  Sarah Blickenstaff
--------------------------
  Maze defines the general structure of a maze: a two-dimensional array of characters.
  Symbols in the array represent a possible path or a blocker.

"""

import random     # random number generator
import copy	      # localCopy = copy.deepcopy(maze)

class Maze:

    def __init__( self, maxRow = 12, maxCol = 12):
        """Create a maze"""
        self.MAXROW = maxRow
        self.MAXCOL = maxCol
        self.POSSIBLEPATH = ' '
        self.BLOCKER      = '*'
        self.THEWAYOUT    = '!'

        self.PATH_BLOCKER_RATIO = 0.5

        self.theMaze = list()

    def _genMaze( self ):
        """Generate a random maze based on probability"""
        localMaze = [['*' for i in range( self.MAXROW )] \
                         for j in range( self.MAXCOL )]

        for row in range( self.MAXROW ):
            for col in range( self.MAXCOL ):
                threshold = random.random()
                if threshold > self.PATH_BLOCKER_RATIO:
                    localMaze[ row ][ col ] = self.POSSIBLEPATH
                else:
                    localMaze[ row ][ col ] = self.BLOCKER

        self.theMaze = localMaze

    def gen_Given_Maze(self, data):
        '''Generates a specific maze based on a given file'''
        localMaze = [[' ' for i in range(self.MAXROW)] \
                     for j in range(self.MAXCOL)]

        for row in range(self.MAXROW):
            for col in range(self.MAXCOL):
                localMaze[row][col] = data[row][col]

        self.theMaze = localMaze

    def __str__( self ):
        """Generate a string representation of the maze"""
        x = ''
        for col in range(self.getColSize()):
            x += str(col%10)
        print (' ' + x)
        x = ''

        for row in range(self.MAXROW):
            for col in range(self.MAXCOL):
                x += str(self.theMaze[row][col])
            x += "\n"

            print(str(row%10) + x)
            x = ''

        return ''

    def getColSize( self ):
        """Return column count"""
        return self.MAXCOL

    def getRowSize( self ):
        """Return row count"""
        return self.MAXROW

    def readMaze( self, fileName ):
        """Reading maze from a file.
           The file should be in the form of a matrix, e.g.,
           ** *
           *  *
           ** *
           ** *
           would be a 4x4 input maze."""
        matrix_data = open(fileName, 'r')
        self.MAXCOl = 0
        self.MAXROW = 0
        elements = []
        data = []

        for row in matrix_data:
            row = row[:-1]
            for col in range(len(row)):
                elements.append(col)
            data.append(row)
            self.MAXROW += 1
            self.MAXCOL = len(row)

        self.theMaze = data
       # self.gen_Given_Maze(data)

    def getMaze( self ):
        """Return a copy of the maze"""
        return copy.deepcopy(self.theMaze)

    def isClear( self, row, col ):
        """Determine if this cell is clear (pathway)."""
        return self.getValue(row, col) == self.POSSIBLEPATH

    def isInMaze( self, row, col ):
        """Determine if a cell is inside the maze."""
        if col < 0 or row < 0:
            return False
        elif row < self.getRowSize() and col < self.getColSize():
            return True
        else:
            return False

    def setValue( self, row, col, value ):
        """Set the value to a cell in the maze."""
        self.theMaze[row][col] = value

    def getValue( self, row, col ):
        """Return the value of the current cell."""
        if self.isInMaze(row, col):
            return self.theMaze[row][col]
        else:
            return None
