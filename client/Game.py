DISCONNECTED_STATE = "DISCONNECTED_STATE"
PLACING_PIECES_STATE = "PLACING PIECES"
PLAYING_GAME_STATE = "PLAYING_GAME"

class GameState(object):
    def __init__(self, currentPlayerId, state = DISCONNECTED_STATE,board=[]):
        if (board == []):
            self.board = self.setupEmptyBoard()
        else:
            self.board = board
        self.lastMove = None
        self.state = state

    def move(self, delta):
        piece = self.board[delta[0]]
        self.board[delta[0]] = None
        self.board[delta[1]] = piece
        self.lastMove = delta

    def placePiece(self,board,piece,row, col):
        if (self.state != PLACING_PIECES_STATE): raise new Exception("cannot set pieces while you're not in placing pieces")
        elif (row,col) in [
        self.board[row][col] = piece
        self.leftoverPieces.remove(piece)

    def getBoard(self):
        return self.board

    def setupEmptyBoard(self):

