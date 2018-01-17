

class board():
    
    def __init__(self):
        self.height = 10
        self.width = 10
        self.board = []
        for i in self.height:
            self.board.append([0] * self.width)

    def checkPiecePlaceable(self, piece):
        for i in self.height:
            for j in self.width:
                if not self._checkPositionValid(piece, i, j):
                    return False
        return True
 
    def placePiece(self, piece, x, y):
       
        if not self._checkPositionValid(piece, x, y):
            raise Exception("unable to place piece at position %s %s" % (x, y) 
        
        for i in range(y, y+piece.height):
            for j in range(x, x+piece.width):
                self.board[i][j] = 1

        clearedRows = self._clearRows()
        return clearedRows 

    def _clearRows(self):
        totalCleared = 0 
        for row in self.board:
            if 0 not in row:
                totalCleared += 1

        for i in self.width:
            tmp = [x[i] for x in self.board]
            if 0 not in tmp:
                totalCleared += 1
        return totalCleared

    def _checkPositionValid(self, piece, x, y):
        
        for i in range(y, y+piece.height):
            for j in range(x, x+piece.width):
                if self.board[i][x]:
                    return False
        return True 
            
class piece():

    def __init__(self, height, width, pieceType):
        self.height = height 
        self.width = width
        self.pieceMap = []
        for i in height:
            self.pieceMap.append([0] * self.width)

        if pieceType == 0:
            self.pieceMap[0][0] = 1
        elif pieceType == 1:
            self.pieceMap[0][0] = 1
            self.pieceMap[0][1] = 1
        elif pieceType == 2:
            self.pieceMap[0][0] = 1
            self.pieceMap[0][1] = 1
            self.pieceMap[0][2] = 1
        elif pieceType == 3:
            self.pieceMap[0][0] = 1
            self.pieceMap[0][1] = 1
            self.pieceMap[0][2] = 1
            self.pieceMap[0][3] = 1
        elif pieceType == 4:
            self.pieceMap[0][0] = 1
            self.pieceMap[0][1] = 1
            self.pieceMap[0][2] = 1
            self.pieceMap[0][3] = 1
            self.pieceMap[0][4] = 1
        elif pieceType == 5:
            self.pieceMap[0][0] = 1
            self.pieceMap[0][1] = 1
            self.pieceMap[1][0] = 1
            self.pieceMap[1][1] = 1
        elif pieceType == 6:
            self.pieceMap[0][0] = 1
            self.pieceMap[0][1] = 1
            self.pieceMap[0][2] = 1
            self.pieceMap[1][0] = 1
            self.pieceMap[1][1] = 1
            self.pieceMap[1][2] = 1
            self.pieceMap[2][0] = 1
            self.pieceMap[2][1] = 1
            self.pieceMap[2][2] = 1











